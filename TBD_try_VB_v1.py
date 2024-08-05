import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import os

# Function to process PDF and create vector store
def process_pdf(uploaded_file):
    # Load the PDF
    loader = PyPDFLoader(uploaded_file)
    documents = loader.load()

    # Split the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200,
        length_function=len
    )
    all_splits = text_splitter.split_documents(documents)

    # Define embeddings and vector store directory
    embeddings = OllamaEmbeddings(base_url="http://localhost:11434", model="nomic-embed-text:latest")
    persist_directory = 'vector_database'

    # Ensure the persistence directory exists
    if not os.path.exists(persist_directory):
        os.makedirs(persist_directory)

    # Create the vector store
    vectorstore = Chroma.from_documents(
        documents=all_splits,
        embedding=embeddings,
        persist_directory=persist_directory
    )

    # Persist the vector store to disk
    vectorstore.persist()

    return vectorstore

# Streamlit app
def main():
    st.title("PDF Embedding and Vector Store")

    # File uploader for PDF
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Save the uploaded file temporarily
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.write("PDF uploaded successfully. Processing...")

        # Process the PDF and create vector store
        vectorstore = process_pdf(uploaded_file.name)

        st.success("Embeddings generated and stored successfully!")

        # Optional: Display some information about the vector store
        st.write("Vector store contains:", len(vectorstore), "documents")

if __name__ == "__main__":
    main()
