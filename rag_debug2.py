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
import json
from typing import List, Dict, Any, Optional
import time
import sys

class PDFQuestionAnsweringSystem:
    def __init__(self) -> None:
        self.vector_db = None
        self.embeddings_data = None
        self.llm_model = "phi3:3.8b-mini-4k-instruct-q4_1"
        self.embedding_model = "nomic-embed-text"
        self.collection_name = "local-rag"
        self.retriever = None

    def load_pdf(self, file_path: str):
        loader = UnstructuredPDFLoader(file_path=file_path)
        return loader.load()

    def split_text(self, data):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        return text_splitter.split_documents(data)

    def add_to_vector_store(self, documents) -> None:
        self.vector_db = Chroma.from_documents(
            documents=documents,
            embedding=OllamaEmbeddings(model=self.embedding_model, show_progress=True),
            collection_name=self.collection_name
        )

    def generate_and_store_embeddings(self, file_path: str) -> None:
        start_time = time.time()
        data = self.load_pdf(file_path)
        chunks = self.split_text(data)
        embeddings = OllamaEmbeddings(model=self.embedding_model, show_progress=True)
        self.embeddings_data = [(chunk, embeddings.embed_documents([chunk.page_content])[0]) for chunk in chunks]
        self.add_to_vector_store(chunks)
        self.retriever = self.vector_db.as_retriever()
        end_time = time.time()
        print(f"PDF processing and embedding time: {end_time - start_time:.2f} seconds")

    def query_llm(self, input_data: Dict[str, Any]) -> str:
        start_time = time.time()
        llm = ChatOllama(model=self.llm_model)
        template = """Answer the question based ONLY on the following context:
        {context}
        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)
        chain = (
            {"context": self.retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        answer = chain.invoke(input_data)
        end_time = time.time()
        print(f"Answer generation time: {end_time - start_time:.2f} seconds")
        return answer

    def upload_and_process_pdf(self, file_path: str) -> None:
        self.generate_and_store_embeddings(file_path)

    def get_embeddings_data(self) -> List[Dict[str, Any]]:
        return [{"text": chunk.page_content, "embedding": embedding} for chunk, embedding in self.embeddings_data]
    
    def get_answer(self, question: str) -> str:
        return self.query_llm({"question": question})

# Streamlit
def main() -> None:
    st.title("PDF Question Answering System")
    st.write("Upload a PDF and ask questions based on its content.")

    system = PDFQuestionAnsweringSystem()

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Save the uploaded PDF
        with open("uploaded_file.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        start_time = time.time()
        system.upload_and_process_pdf("uploaded_file.pdf")
        end_time = time.time()
        st.write(f"PDF upload and processing time: {end_time - start_time:.2f} seconds")
        st.write("Embeddings generated and stored successfully.")

        # Option to download the embeddings data
        embeddings_data = system.get_embeddings_data()
        embeddings_json = json.dumps(embeddings_data, indent=4)
        st.download_button("Download Embeddings Data", embeddings_json, "embeddings.json")

        question = st.text_input("Ask a question based on the uploaded PDF")

        if st.button("Get Answer"):
            if question:
                answer = system.get_answer(question)
                st.write(answer)
            else:
                st.write("Please enter a question.")

        if st.button("Clear Database"):
            system.delete_collection()
            st.write("Vector database cleared.")

if __name__ == "__main__":
    main()
