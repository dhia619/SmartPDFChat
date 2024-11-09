from langchain_community.llms.ollama import Ollama
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate

class RAGHandler:
    def __init__(self):
            
        self.PROMPT_TEMPLATE = """
        Answer the question based only on the following context:

        {context}

        ---

        Answer the question based on the above context: {question}
        """


    def query_rag(self, query_text: str, db: Chroma):

        # Search the DB.
        results = db.similarity_search_with_score(query_text, k=5)
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        prompt_template = ChatPromptTemplate.from_template(self.PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query_text)
        # print(prompt)
        
        model = Ollama(model="granite3-dense")
        response_text = model.invoke(prompt)

        sources = [doc.metadata.get("id", None) for doc, _score in results]
        formatted_response = f"Response: {response_text}\nSources: {sources}"

        return response_text, formatted_response