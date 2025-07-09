import os
import chromadb
from chromadb.config import Settings
from chromadb import PersistentClient
import os
import openai
import json
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Fetch GROQ API key from environment variable
GROQ_API_KEY= os.getenv("GROQ_API_KEY")

# Using Chroma DB with Persistant Storage

# Setup Persistent Chroma Client (stores data in current path)
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory
db_path = os.path.join(current_dir, "chroma_db_storage")  # Path for DB storage

# Create persistent client for Chroma DB
client = PersistentClient(path=db_path, settings=Settings(anonymized_telemetry=False))

# Get or create a vector collection named "main_content"
collection = client.get_or_create_collection(name="main_content")

# Load JSON data from file
with open('data.json', 'r') as f:
    documents = json.load(f)

# Prepare document IDs and content
ids = []
final_content = []
for i in documents:
    id = "text_" + str(i["id"])   # Create unique ID for each document
    content = i["text"]           # Extract document content
    ids.append(id)
    final_content.append(content)

# Add data to vector DB only if collection is empty
if collection.count() == 0:
    collection.add(documents=final_content, ids=ids)
    print("Added data to persistent vector DB.")
else:
    print("Vector DB already contains data. Skipping addition.")

# Search Function: queries Chroma vector DB
def search_data(user_query, top_k=5):
    user_input = str(user_query["Query"])  # Extract query text
    results = collection.query(query_texts=[user_input], n_results=top_k)
    matched_data = results['documents'][0]
    scores = results['distances'][0]  # Lower score = better match
    return list(zip(matched_data, scores))

# Summarize matched content using Groq LLM
def summarize_details(text, query):
    client = Groq(api_key=GROQ_API_KEY)
    chat_completion = client.chat.completions.create(
    messages=[
        # System message to define assistant behavior
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        # User prompt with query and context
        {
            "role": "user",
            "content": f"""
                Query: {query}
                Context: {text}

                Based on **Query**, generate a detail but informative summary using given **Context** only.

            Note: Do't take any information from any other resources only just given **Context** data to generate final summary.
            """
        }
    ],

    # Define Groq LLM model to use
    model="llama-3.3-70b-versatile"
    )

    # Extract and return the summary content
    text = chat_completion.choices[0].message.content
    return {"summary": text}

# Main execution block
if __name__ == "__main__":
    user_input = input("Enter your query to search: ")  # Take user query from input
    user_query = {"Query": f"{user_input}"}   # Wrap input in a dictionary
    matches = search_data(user_query, top_k=5)

    print("\nTop Match:")
    print(f"{matches[0][0]} (score: {matches[0][1]:.4f})")

    print("\nAll Matches:")
    for data, score in matches:
        print(f"{data} (score: {score:.4f})")

    print("\nRestructured the extracted content from Vector DB, by using Groq LLM model to generate final summary result:")
    context_details = []
    for context in matches:
        context_details.append(context[0])  # Extract only the text portion
    
    result = summarize_details(matches, user_input)  # Generate summary using Groq
    print(json.dumps(result, indent=2))  # Pretty print result
