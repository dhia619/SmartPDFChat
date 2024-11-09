import streamlit as st
from documentHandler import DocumentHandler
from chromaDBHandler import ChromaDBHandler
from ragHandler import RAGHandler

# Initialize document handler, database handler, and RAG handler
document_handler = DocumentHandler()
db_handler = ChromaDBHandler("db")
rag_handler = RAGHandler()

# Set up the Streamlit app
st.title("Chat with PDF")

# File uploader for PDF files
uploaded_files = st.file_uploader("Upload a PDF file", type=["pdf"], accept_multiple_files=True)

# Load the documents into the database if files are uploaded
if uploaded_files:
    # Process uploaded PDFs and add to database
    docs = document_handler.load_documents(uploaded_files)
    chunks = document_handler.add_ids_to_chunks(document_handler.split_documents(docs))
    db_handler.add_to_chromadb(chunks)
    st.success("PDF file has been successfully processed and loaded into the database!")

# Chat interface
prompt = st.chat_input("Type your prompt here")

# Create a list of messages in the session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Load the chat history
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Display the prompt and the response each time the user sends a new prompt
if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    rag_response = rag_handler.query_rag(prompt, db_handler.db)[0]
    st.chat_message("ai").markdown(rag_response)
    st.session_state.messages.append({'role': 'ai', 'content': rag_response})
