import os
import openai
import streamlit as st
from llama_index.core import GPTVectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core import Settings
from llama_index.embeddings.openai import OpenAIEmbedding

# Load OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Set the embedding model
Settings.embed_model = OpenAIEmbedding()

# Load stored index
storage_context = StorageContext.from_defaults(persist_dir="./index_storage")
index = load_index_from_storage(storage_context)

# Set up Streamlit UI
st.title("CCU GPT")
st.write("Ask me anything based on the uploaded documents!")

# User input
user_query = st.text_input("Enter your question:")

if user_query:
    # Query the index
    response = index.as_query_engine().query(user_query)
    st.write("### Answer:")
    st.write(response.response)

