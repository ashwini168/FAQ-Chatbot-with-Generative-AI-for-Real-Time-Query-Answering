# Write Streamlit app code to a file
with open('app.py', 'w') as f:
    f.write("""
import streamlit as st
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd
from transformers import pipeline

# Function to load data with encoding fix
@st.cache
def load_data():
    try:
        return pd.read_csv('code.csv', encoding='utf-8')
    except UnicodeDecodeError:
        # Fallback to a different encoding if UTF-8 fails
        return pd.read_csv('code.csv', encoding='latin1')

# Load pre-saved embeddings and index
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = np.load('embeddings.npy')
index = faiss.read_index('faiss_index.bin')

# Load FAQ data
df = load_data()

# Initialize a generative AI model
qa_pipeline = pipeline('text-generation', model='gpt2')

# Streamlit app layout
st.title("FAQ Chatbot with Generative AI")
st.write("Ask a question below:")

# User input
question = st.text_input("Your Question:")
if question:
    # Generate embedding for user question
    question_embedding = model.encode([question])

    # Perform similarity search
    D, I = index.search(question_embedding, k=1)

    # Fetch the best match from the dataframe
    closest_match = df.iloc[I[0][0]]['response']

    # Generate a dynamic response using a generative model
    prompt = f"Answer the following question based on the context: '{question}'. Provide a helpful, clear, and realistic response based on common knowledge about bootcamps and job preparation."
    dynamic_answer = qa_pipeline(prompt)[0]['generated_text']

    # Display the results
    st.write(f"You asked: {question}")
    st.write(f"Closest FAQ match: {closest_match}")
    st.write(f"Generative AI answer: {dynamic_answer}")
""")
