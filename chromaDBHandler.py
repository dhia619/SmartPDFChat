from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain.schema.document import Document
import shutil

class ChromaDBHandler:

    def __init__(self, CHROMA_PATH: str):

        self.CHROMA_PATH = CHROMA_PATH
        self.create_or_load_DB()

    def create_or_load_DB(self):
        self.db = Chroma(
            persist_directory=self.CHROMA_PATH, embedding_function=self.get_embedding_function("granite3-dense")
        )

    def add_to_chromadb(self, chunks: list[Document]):

        # Add or Update the documents.
        existing_items = self.db.get(include=[])
        existing_ids = set(existing_items["ids"])
        print(f"Number of existing documents in DB: {len(existing_ids)}")

        # Only add documents that don't exist in the DB.
        new_chunks = []
        for chunk in chunks:
            if chunk.metadata["id"] not in existing_ids:
                new_chunks.append(chunk)

        if len(new_chunks):
            print(f"👉 Adding new documents: {len(new_chunks)}")
            new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
            self.db.add_documents(new_chunks, ids=new_chunk_ids)
            self.db.persist()
        else:
            print("✅ No new documents to add")

    def get_embedding_function(self, model: str) -> OllamaEmbeddings:
        
        embeddings = OllamaEmbeddings(model=model)

        return embeddings
    
    def delete_db(self):
        shutil.rmtree("db")