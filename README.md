# SmartPDFChat

An intelligent document-based chatbot using Retrieval-Augmented Generation (RAG) to answer queries from uploaded PDF files.

## Features

- **Upload Documents**: Supports uploading PDFs to extract information.
- **Query-Based Responses**: Ask questions and get responses based on the uploaded content.
- **Streamlit Interface**: Simple, interactive web app interface.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dhia619/SmartPDFChat.git
   cd SmartPDFChat
   ```
2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Install Ollama and Download Model**
   - Visit [Ollama's download page](https://ollama.com/download) and install the application on your system.
   - After installing, download an open-source language model from their library. For this project, you can use the [IBM Granite3-Dense model](https://ollama.com/library/granite3-dense)

## Usage

```bash
streamlit run src/main.py
```
