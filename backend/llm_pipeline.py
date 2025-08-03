from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_core.prompts import PromptTemplate
from CRLLM import HFBBLLM
from file_utilities import chunks_merger
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def answer_question(document_text: str, question: str) -> str:
    """
    Takes document text and a user query, and returns the generated answer.
    """
    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.create_documents([document_text])

    # Create embeddings and vector store
    embedding_model = HuggingFaceEndpointEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2"
    )
    vector_store = FAISS.from_documents(chunks, embedding_model)

    # Retrieve context for the query
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    # results = retriever.invoke(user_query)
    # context = "\n\n".join(doc.page_content for doc in results)

    parallel_chain = RunnableParallel({
        'context' : retriever | RunnableLambda(chunks_merger),
        'question' : RunnablePassthrough()
    })
    # Set up LLM
    llm = HFBBLLM("HuggingFaceH4/zephyr-7b-beta")

    # Set up Prompt
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
        You are an efficient, honest expert AI assistant. Use the following context to answer the user's question in best way possible wthout hallucination and only using fact in provided context.
        If the context does not contain the answer or nothing can be concretely said using the contenta about the query,then politely say "I don't know."Also judge and tell the degree upto which the user can depend on the effcency of your answer usng context.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    )
    
    parser = StrOutputParser()
    # Generate answer
    genchain = parallel_chain | prompt | llm | parser
    output = genchain.invoke(question)

    return output

# # Example usage
# if __name__ == "__main__":
#     text = """<--- tumhara bada document yaha paste karo --->"""
#     query = "What are ores of Uranium?"
#     answer = answer_question(text, query)
#     print("Answer:", answer)
