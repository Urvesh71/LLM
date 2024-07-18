import streamlit as st
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_community.document_loaders import PyPDFLoader
import tempfile

class Chatbot:
    def __init__(self, file_path, chunk_size=7500, chunk_overlap=100, model="nomic-embed-text", local_model="mistral"):
        self.file_path = file_path
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.embedding_model = model
        self.local_model = local_model

        self.loader = PyPDFLoader(file_path)
        self.pages = self.loader.load_and_split()
        self.chunks = self._split_and_chunk()
        self.vector_db = self._create_vector_db()
        self.llm = ChatOllama(model=self.local_model)
        self.retriever = self._create_retriever()
        self.prompt = self._create_prompt_template()
        self.chain = self._create_chain()

    def _split_and_chunk(self):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        return text_splitter.split_documents(self.pages)

    def _create_vector_db(self):
        st.info("Creating vector database...")
        vector_db = Chroma.from_documents(
            documents=self.chunks, 
            embedding=OllamaEmbeddings(model=self.embedding_model, show_progress=True),
            collection_name="local-rag"
        )
        st.success("Vector database created successfully.")
        return vector_db

    def _create_retriever(self):
        QUERY_PROMPT = PromptTemplate(
            input_variables=["question"],
            template="""You are an AI language model assistant. Your task is to generate five
            different versions of the given user question to retrieve relevant documents from
            a vector database. By generating multiple perspectives on the user question, your
            goal is to help the user overcome some of the limitations of the distance-based
            similarity search. Provide these alternative questions separated by newlines.
            Original question: {question}"""
        )
        return MultiQueryRetriever.from_llm(
            self.vector_db.as_retriever(), 
            self.llm,
            prompt=QUERY_PROMPT
        )

    def _create_prompt_template(self):
        template = """Answer the question based ONLY on the following context:
        {context}
        Question: {question}
        """
        return ChatPromptTemplate.from_template(template)

    def _create_chain(self):
        return (
            {"context": self.retriever, "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

    def get_response(self, user_input):
        return self.chain.invoke({"question": user_input})

@st.cache_resource
def create_chatbot(file_path):
    return Chatbot(file_path=file_path)

@st.cache_resource
def create_vector_db(chunks, embedding_model):
    return Chroma.from_documents(
        documents=chunks, 
        embedding=OllamaEmbeddings(model=embedding_model, show_progress=True),
        collection_name="local-rag"
    )

def main():
    st.title("PDF Chatbot")
    st.write("Upload a PDF file and ask questions to the chatbot.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        st.success("File uploaded successfully!")

        # Initialize Chatbot only once per upload
        chatbot = create_chatbot(file_path=temp_file_path)

        # Cache the vector database creation
        chatbot.vector_db = create_vector_db(chatbot.chunks, chatbot.embedding_model)

        user_input = st.text_input("Ask a question:")
        if user_input:
            response = chatbot.get_response(user_input)
            st.write("Response:", response)

if __name__ == "__main__":
    main()