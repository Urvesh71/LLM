# Use the official Python image from Docker Hub
FROM python:3.13.0rc1-slim

# Set the working directory
WORKDIR /app

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    sqlite3 \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the application code
COPY . /app/

# Install the dependencies
RUN pip install chromadb
RUN pip install streamlit
RUN pip install langchain_core
RUN pip install langchain_community
RUN pip install PyPDF2
RUN pip install pypdf

# Expose the port
EXPOSE 8501
EXPOSE 11434

# Run the application
# CMD ["streamlit", "rag_app_debugging1.py"]
CMD ["streamlit", "run", "streamlit_RAG.py", "--server.port=8501", "--server.address=0.0.0.0"]