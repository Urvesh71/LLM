import streamlit as st
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever
from typing import List, Dict

# Interface Segregation Principle: Define interfaces for different components
class PDFLoaderInterface:
    def load(self, file_path: str) -> List[Dict]:
        pass

class TextSplitterInterface:
    def split_documents(self, data: List[Dict]) -> List[Dict]:
        pass

class VectorStoreInterface:
    def add_documents(self, documents: List[Dict], embedding_model: str, collection_name: str):
        pass

class LLMInterface:
    def query(self, input_data: Dict) -> str:
        pass

# Single Responsibility Principle: Concrete implementations of the interfaces
class PDFLoader(PDFLoaderInterface):
    def load(self, file_path: str) -> List[Dict]:
        loader = UnstructuredPDFLoader(file_path=file_path)
        return loader.load()

class TextSplitter(TextSplitterInterface):
    def split_documents(self, data: List[Dict]) -> List[Dict]:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=7500, chunk_overlap=100)
        return text_splitter.split_documents(data)

class VectorStore(VectorStoreInterface):
    def __init__(self):
        self.vector_db = None

    def add_documents(self, documents: List[Dict], embedding_model: str, collection_name: str):
        self.vector_db = Chroma.from_documents(
            documents=documents, 
            embedding=OllamaEmbeddings(model=embedding_model, show_progress=True),
            collection_name=collection_name
        )

    def get_retriever(self):
        return self.vector_db.as_retriever()

    def delete_collection(self):
        if self.vector_db:
            self.vector_db.delete_collection()

class LLM(LLMInterface):
    def __init__(self, model: str):
        self.llm = ChatOllama(model=model)
        self.retriever = None

    def set_retriever(self, retriever):
        self.retriever = retriever

    def query(self, input_data: Dict) -> str:
        template = """Answer the question based ONLY on the following context:
        {context}
        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)
        chain = (
            {"context": self.retriever, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        return chain.invoke(input_data)

class PDFQuestionAnsweringSystem:
    def __init__(self):
        self.loader = PDFLoader()
        self.splitter = TextSplitter()
        self.vector_store = VectorStore()
        self.llm = LLM(model="mistral")

    def upload_and_process_pdf(self, file_path: str):
        data = self.loader.load(file_path)
        chunks = self.splitter.split_documents(data)
        self.vector_store.add_documents(documents=chunks, embedding_model="nomic-embed-text", collection_name="local-rag")
        retriever = self.vector_store.get_retriever()
        self.llm.set_retriever(MultiQueryRetriever.from_llm(retriever, self.llm.llm, self._query_prompt_template()))

    def _query_prompt_template(self):
        return PromptTemplate(
            input_variables=["question"],
            template="""You are an AI language model assistant. Your task is to generate five
            different versions of the given user question to retrieve relevant documents from
            a vector database. By generating multiple perspectives on the user question, your
            goal is to help the user overcome some of the limitations of the distance-based
            similarity search. Provide these alternative questions separated by newlines.
            Original question: {question}"""
        )

    def get_answer(self, question: str) -> str:
        return self.llm.query({"question": question})

    def clear_database(self):
        self.vector_store.delete_collection()

# Streamlit App
def main():
    st.title("PDF Question Answering System")
    st.write("Upload a PDF and ask questions based on its content.")

    system = PDFQuestionAnsweringSystem()

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Save the uploaded PDF
        with open("uploaded_file.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        system.upload_and_process_pdf("uploaded_file.pdf")

        question = st.text_input("Ask a question based on the uploaded PDF")

        if st.button("Get Answer"):
            if question:
                answer = system.get_answer(question)
                st.write(answer)
            else:
                st.write("Please enter a question.")

        if st.button("Clear Database"):
            system.clear_database()
            st.write("Vector database cleared.")

if __name__ == "__main__":
    main()
