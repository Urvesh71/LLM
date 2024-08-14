import chromadb
from chromadb.utils import embedding_functions
from langchain_community.llms import Ollama
from langchain_community.embeddings.ollama import OllamaEmbeddings
# from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import json
import numpy as np
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.retrievers import MultiQueryRetriever
# from langchain_community.llms import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_chroma import Chroma

# Define models as constants for easy configuration
EMBEDDING_MODEL = "nomic-embed-text:latest"
BASE_URL = "http://localhost:11434"
LLM_MODEL = "mistral:latest"

# Function to load and parse the JSON file
def load_json_file(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

# Function to chunk the JSON data
def chunk_json_data(data):
    chunks = []
    for cycle in data:
        cycle_text = f"Cycle: {cycle['cycle']}, Start Date: {cycle['sdate']}, Text: {cycle['Text']}"
        for segment in cycle['Segments']:
            segment_text = (
                f"Segment {segment['Seqnr']} - {segment['SegmentHeader']['Name']}: "
                f"{segment['SegmentHeader']['Text']} "
                f"Cost Element: {segment['SegmentHeader']['CostElement']}\n"
                f"Players: {', '.join([player['Player'] for player in segment['Players']])}\n"
                f"Sender Values: {segment['SenderValues']}\n"
                f"Receiver Values: {segment['ReceiverValues']}"
            )
            chunks.append(cycle_text + "\n" + segment_text)
    return chunks

file_path = 'Cycles schema 01.json'

data = load_json_file(file_path)

chunks = chunk_json_data(data)

embedding_function = OllamaEmbeddings(
    base_url=BASE_URL,
    model=EMBEDDING_MODEL
)

# Initialize Chroma client
client = chromadb.Client()

# Create a collection in Chroma
collection = client.create_collection(name="my_collection")

# Generate embeddings for each chunk and store them in Chroma
for i, chunk in enumerate(chunks):
    embedding = embedding_function.embed_query(chunk)
    collection.add(
        embeddings=[embedding],  # embedding vector
        metadatas=[{"text": chunk}],  # metadata to store the original chunk text
        ids=[f"chunk_{i}"]  # unique ID for each chunk
    )

print(f'Embeddings are created and stored in Chroma. Collection size: {collection.count()}')

# Initialize the vector store retriever
vector_db = Chroma(
    collection_name="my_collection", 
    client=client, 
    embedding_function=embedding_function,
    persist_directory='vector_database'
)

vector_db.persist()

# # Setup the local model for the LLM (mistral)
# llm = Ollama(model=LLM_MODEL)

# # Define the prompt for generating alternative queries
# QUERY_PROMPT = PromptTemplate(
#     input_variables=["question"],
#     template="""You are an AI language model assistant. Your task is to generate five
#     different versions of the given user question to retrieve relevant documents from
#     a vector database.ö By generating multiple perspectives on the user question, your
#     goal is to help the user overcome some of the limitations of the distance-based
#     similarity search. Provide these alternative questions separated by newlines.
#     Original question: {question}""",
# )

# # Create the multi-query retriever
# retriever = MultiQueryRetriever.from_llm(
#     retriever=vector_db.as_retriever(), 
#     llm=llm,
#     prompt=QUERY_PROMPT
# )

# # Define the RAG prompt
# template = """Answer the question based ONLY on the following context:
# {context}
# Question: {question}
# """

# prompt = ChatPromptTemplate.from_template(template)

# # Setup the chain
# chain = (
#     {"context": retriever, "question": RunnablePassthrough()}
#     | prompt
#     | llm
#     | StrOutputParser()
# )

# # Run the chain with user input
# response = chain.invoke(input("Enter your question: "))
# print(response)