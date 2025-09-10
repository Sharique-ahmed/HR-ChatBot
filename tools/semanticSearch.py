import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from langchain.tools import StructuredTool


def semanticSerchTopEmployees(query):
    """
    Simple semantic search tool for employee dataset.
    
    Args:
        query (str): User query.
        json_path (str): Path to employee JSON with embeddings.
        top_k (int): Number of top results to return.
    
    Returns:
        List[dict]: Top employees without embeddings.
    """
    # -----------------------------
    # 1️⃣ Load employee JSON
    # -----------------------------
    with open("SampleDatatset\employees_with_embeddings.json", "r") as f:
        data = json.load(f)
    employees = data["employees"]
    
    # -----------------------------
    # 2️⃣ Load embeddings
    # -----------------------------
    embeddings = np.array([emp["embedding"] for emp in employees], dtype=np.float32)
    
    # -----------------------------
    # 3️⃣ Create FAISS index
    # -----------------------------
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)  # cosine similarity
    index.add(embeddings)
    
    # -----------------------------
    # 4️⃣ Embed user query
    # -----------------------------
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_emb = model.encode([query], convert_to_numpy=True, normalize_embeddings=True)
    
    # -----------------------------
    # 5️⃣ Search top_k
    # -----------------------------
    D, I = index.search(query_emb, 3)
    
    # -----------------------------
    # 6️⃣ Map top results
    # -----------------------------
    top_employees = []
    for i in I[0]:
        emp = employees[i].copy()
        emp.pop("embedding", None)  # remove embedding before returning
        top_employees.append(emp)
    
    return top_employees



semanticSearchTool = StructuredTool.from_function(
    func=semanticSerchTopEmployees,
    name="semantic_search",
    description="""
        - Understand the query and give only the important fields to the tool
        - Search employees semantically based on user query. 
        - Returns top 3 most relevant employees with all info except embeddings.
    """
)