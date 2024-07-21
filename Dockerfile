# Use the official Python image from the Docker Hub
FROM python:3.13.0b3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    tesseract-ocr \
    tesseract-ocr-eng \
    libtesseract-dev \
    pkg-config \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file into the container
COPY rewuirements.txt ./
RUN pip install --no-cache-dir -r rewuirements.txt

# Expose the port Streamlit will run on
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "rag_debug2.py"]
