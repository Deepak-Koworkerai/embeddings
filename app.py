from flask import Flask, request, jsonify
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

# Initialize the Flask app
app = Flask(__name__)

model_name = "BAAI/bge-base-en"
encode_kwargs = {'normalize_embeddings': True} # set True to compute cosine similarity

# Creating an object for embedding model
embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs={'device': 'cpu'},  # use cuda, if gpu is available
    encode_kwargs=encode_kwargs
)

@app.route("/embeddings", methods=["POST"])
def get_embeddings():
  return embeddings
  
