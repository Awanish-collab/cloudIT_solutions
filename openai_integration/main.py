from dotenv import load_dotenv
import os
from groq import Groq

''' Here, using Groq API instead of OpenAI API '''
load_dotenv()

# Fetch GROQ API key from environment variable
GROQ_API_KEY= os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)  # creating client to communicate with Groq API models

def summary_with_groq_model(text_content):
    chat_completion = client.chat.completions.create(
    messages=[
        # Set an optional system message. This sets the behavior of the
        # assistant and can be used to provide specific instructions for
        # how it should behave throughout the conversation.
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        # Set a user message for the assistant to respond to.
        {
            "role": "user",
            "content": f"""Generate final summary for given content: {text_content}""",
        }
    ],

    # The language model which will generate the completion.
    model="llama-3.3-70b-versatile"
    )

    # Print the completion returned by the LLM.
    #print(chat_completion.choices[0].message.content)
    response = chat_completion.choices[0].message.content
    return response

#text_content = input("Enter you content:") # for user input
text_content = """
What is RAG? 
        Retrieval-Augmented Generation is an AI technique that combines search-based retrieval with generative 
        models (like GPT or Claude). It helps generate more accurate, context-aware, and up-to-date responses by 
        fetching relevant knowledge from external sources before generation. 
        Retrieval-Augmented Generation (RAG) is a technique in natural language processing that enhances the capabilities 
        of generative models by integrating them with retrieval systems.   
    
    RAG Pipeline — Key Steps: 
        1. User Query Input 
        The user provides a question or prompt. 
        2. Retrieval (Search) 
        The system searches a knowledge base, documents, or vector database to find relevant context 
        chunks using similarity search. 
        3. Augmentation 
        Retrieved documents are combined with the original query and passed to the language model. 
        4. Generation 
        The language model (e.g., GPT, Claude, etc.) uses both the query and retrieved context to generate a 
        more relevant and grounded response. 
    
    Why RAG? 
        • Improves factual accuracy 
        • Reduces hallucinations 
        • Can reference private or recent knowledge not in the model's training data

    Semantic Search 
        Semantic search uses the meaning of the text rather than exact keywords to find relevant information. It's 
        typically powered by embeddings—vectors that represent the meaning of a chunk of text. It also 
        understand the Synonyms of words in deep way but similar search can also understand but on the 
        surface level only. 
        • Example: If you search "How to fix a leaking faucet?", semantic search might retrieve chunks that 
        contain "repair dripping tap" because the intent and meaning are similar. 
        • Tools involved: Sentence Transformers, FAISS, Chroma, Qdrant, etc. 
        • Common in RAG: Used to retrieve context from vector databases based on the question's meaning. 
"""
final_summary = summary_with_groq_model(text_content)
print("Summary:\n", "-"*50, "\n", final_summary)        




# Below Implementation with FastAPI Endpoint with OpenAI
'''from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import openai, os

load_dotenv()  # Load .env
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/generate_summary")
async def generate_summary(input: InputText):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Summarize this: {input.text}"}]
        )
        summary = response.choices[0].message.content.strip()
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
'''
