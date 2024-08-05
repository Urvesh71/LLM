import streamlit as st
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnableMap, RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_community.document_loaders import PyPDFLoader
import tempfile
import os

class Chatbot:
    def __init__(self, file_path, chunk_size=7500, chunk_overlap=100, model="nomic-embed-text", local_model="mistral:latest", persist_directory="vector_store"):
        self.file_path = file_path
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.embedding_model = model
        self.local_model = local_model
        self.persist_directory = persist_directory  # Custom directory for vector storage

        # Load and split PDF into pages and chunks
        self.loader = PyPDFLoader(file_path)
        self.pages = self.loader.load_and_split()
        self.chunks = self._split_and_chunk()

        # Create a vector database from document chunks
        self.vector_db = self._create_vector_db()

        # Initialize the language model for answering queries
        self.llm = ChatOllama(model=self.local_model)

        # Create a retriever for querying the vector database
        self.retriever = self._create_retriever()

        # Create a prompt template for generating answers
        self.prompt = self._create_prompt_template()

        # Create a chain for the entire process
        self.chain = self._create_chain()

    def _split_and_chunk(self):
        # Use RecursiveCharacterTextSplitter for chunking documents
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        return text_splitter.split_documents(self.pages)

    def _create_vector_db(self):
        # Ensure the persistence directory exists
        if not os.path.exists(self.persist_directory):
            os.makedirs(self.persist_directory)

        # Generate embeddings for document chunks and create a Chroma vector store with the custom directory
        return Chroma.from_documents(
            documents=self.chunks, 
            embedding=OllamaEmbeddings(model=self.embedding_model, show_progress=True),
            collection_name="local-rag",
            persist_directory=self.persist_directory  # Specify custom directory here
        )

    def _create_retriever(self):
        # Define a query prompt for generating multiple query versions
        QUERY_PROMPT = PromptTemplate(
            input_variables=["question"],
            template="""You are an AI language model assistant. Your task is to generate five
            different versions of the given user question to retrieve relevant documents from
            a vector database. By generating multiple perspectives on the user question, your
            goal is to help the user overcome some of the limitations of the distance-based
            similarity search. Provide these alternative questions separated by newlines.
            Original question: {question}"""
        )
        # Create a MultiQueryRetriever to enhance query retrieval
        return MultiQueryRetriever.from_llm(
            retriever=self.vector_db.as_retriever(), 
            llm=self.llm,
            prompt=QUERY_PROMPT
        )

    def _create_prompt_template(self):
        # Define a prompt template for generating answers based on retrieved context
        template = """Answer the question based ONLY on the following context:
        {context}
        Question: {question}
        """
        return ChatPromptTemplate.from_template(template)

    def _create_chain(self):
        # Create a RAG chain combining context retrieval, prompting, and language modeling
        return RunnableMap(
            {
                "context": self.retriever,
                "question": RunnablePassthrough()
            }
        ) | self.prompt | self.llm | StrOutputParser()

    def get_response(self, user_input):
        # Invoke the chain to get a response for the given user input
        response = self.chain.invoke({"question": user_input})
        return response['content'] if isinstance(response, dict) else response

def main():
    st.title("PDF Chatbot")
    st.write("Upload a PDF file and ask questions to the chatbot.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        # Create a temporary file to store the uploaded PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        st.success("File uploaded successfully!")

        # Specify a custom directory for vector storage
        custom_vector_directory = "custom_vector_storage"

        # Initialize the chatbot with the uploaded file and custom vector directory
        chatbot = Chatbot(file_path=temp_file_path, persist_directory=custom_vector_directory)

        user_input = st.text_input("Ask a question:")
        if user_input:
            # Get a response from the chatbot for the user's question
            response = chatbot.get_response(user_input)
            st.write("Response:", response)

        # Clean up the temporary file after processing
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

if __name__ == "__main__":
    main()
