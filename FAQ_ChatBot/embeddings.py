from sentence_transformers import SentenceTransformer

# Initialize the model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Generate embeddings for the prompts
embeddings = model.encode(df['prompt'].tolist(), show_progress_bar=True)

# Save embeddings for later use
import numpy as np
np.save('embeddings.npy', embeddings)
