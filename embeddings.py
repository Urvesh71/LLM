import chromadb
from chromadb.utils import embedding_functions
from langchain_community.llms import Ollama
from langchain_community.embeddings.ollama import OllamaEmbeddings
# from langchain.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
import json
import numpy as np
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

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

# Initialize the Chroma store as the retriever
retriever = Chroma(collection_name="my_collection", client=client, embedding_function=embedding_function)

llm = Ollama(base_url=BASE_URL, 
             model=LLM_MODEL, 
             verbose=True, 
             callback_manager=CallbackManager(
                 [StreamingStdOutCallbackHandler()]),
            )

rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"  # Use 'stuff', 'map_reduce', or 'map_rerank' depending on your use case
)

query = "What are the cost elements in the data?"
answer = rag_chain.run(query)

print("Answer:", answer)