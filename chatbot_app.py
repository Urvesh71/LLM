"""
Created by: Urveshkumar Koshti
Purpose of the code: To create the Chatbot for the Question-Answer based on the PDF. 
Attributes of the Local Chatbot: 
                        -->  Input to the Code (via Frontend interface): PDF file
                             Output from the code (on the Frontend interface): Text Generation
                        --> Saves the Chat History
                        --> Creates the Vector Database using SQL
                        --> Uses the same Vector Database For the Questions from the same PDF until new PDF is not uploaded by User
To run the File in Docker container: 
                        --> Pull the image from the Docker Hub and then Run the Image. 
                        --> Open the Chatbot by typing 'streamlit run 'Chatbot_app.py'.
"""

from langchain.chains import RetrievalQA
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
from langchain_community.llms import Ollama
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
import streamlit as st
import os
import time

if not os.path.exists('files'):
    os.mkdir('files')

if not os.path.exists('vector_database'):
    os.mkdir('vector_database')

if 'template' not in st.session_state:
    st.session_state.template = """You are a knowledgeable chatbot, here to help with questions of the user. Your tone should be professional and informative.

    Context: {context}
    History: {history}

    User: {question}
    Chatbot:"""
if 'prompt' not in st.session_state:
    st.session_state.prompt = PromptTemplate(
        input_variables=["history", "context", "question"],
        template=st.session_state.template,
    )
if 'memory' not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="history",
        return_messages=True,
        input_key="question")
if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = Chroma(persist_directory='jj',
                                          embedding_function=OllamaEmbeddings(base_url='http://localhost:11434',
                                                                              model="mistral")
                                          )
if 'llm' not in st.session_state:
    st.session_state.llm = Ollama(base_url="http://localhost:11434",
                                  model="mistral",
                                  verbose=True,
                                  callback_manager=CallbackManager(
                                      [StreamingStdOutCallbackHandler()]),
                                  )

# Function to clear the current vector store and reset session state variables
def clear_vectorstore():
    if 'vectorstore' in st.session_state:
        del st.session_state['vectorstore']
    if 'retriever' in st.session_state:
        del st.session_state['retriever']
    if 'qa_chain' in st.session_state:
        del st.session_state['qa_chain']
    if 'chat_history' in st.session_state:
        st.session_state.chat_history = []

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.title("PDF Chatbot")

# Upload a PDF file
uploaded_file = st.file_uploader("Upload your PDF", type='pdf')

if uploaded_file is not None:
    if 'current_pdf' not in st.session_state or st.session_state.current_pdf != uploaded_file.name:
        clear_vectorstore()
        st.session_state.current_pdf = uploaded_file.name
        with st.status("Analyzing your document..."):
            bytes_data = uploaded_file.read()
            with open("files/" + uploaded_file.name + ".pdf", "wb") as f:
                f.write(bytes_data)
            loader = PyPDFLoader("files/" + uploaded_file.name + ".pdf")
            data = loader.load()

            # Initialize text splitter
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1500,
                chunk_overlap=200,
                length_function=len
            )
            all_splits = text_splitter.split_documents(data)

            # Create and persist the vector store
            st.session_state.vectorstore = Chroma.from_documents(
                documents=all_splits,
                embedding=OllamaEmbeddings(model="mistral")
            )
            st.session_state.vectorstore.persist()

        st.session_state.retriever = st.session_state.vectorstore.as_retriever()
        st.session_state.qa_chain = RetrievalQA.from_chain_type(
            llm=st.session_state.llm,
            chain_type='stuff',
            retriever=st.session_state.retriever,
            verbose=True,
            chain_type_kwargs={
                "verbose": True,
                "prompt": st.session_state.prompt,
                "memory": st.session_state.memory,
            }
        )

# Display chat history and handle user input
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["message"])

if user_input := st.chat_input("You:", key="user_input"):
    user_message = {"role": "user", "message": user_input}
    st.session_state.chat_history.append(user_message)
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Assistant is typing..."):
            response = st.session_state.qa_chain(user_input)
        message_placeholder = st.empty()
        full_response = ""
        for chunk in response['result'].split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    chatbot_message = {"role": "assistant", "message": response['result']}
    st.session_state.chat_history.append(chatbot_message)

else:
    st.write("Please upload a PDF file.")
