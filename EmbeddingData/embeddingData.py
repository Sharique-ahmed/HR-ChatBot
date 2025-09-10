import json
from sentence_transformers import SentenceTransformer

# Load employee JSON
with open("employees_dataset.json", "r") as f:
    data = json.load(f)

employees = data["employees"]

# Initialize model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Compute embeddings and add to each employee
for emp in employees:
    text = f"Name: {emp['name']}. Skills: {', '.join(emp['skills'])}. " \
           f"Experience: {emp['experience_years']} years. Projects: {', '.join(emp['projects'])}."
    
    emb = model.encode(text, convert_to_numpy=True, normalize_embeddings=True)
    emp["embedding"] = emb.tolist()  # store as list so JSON serializable

# Save back to JSON
with open("employees_with_embeddings.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"Saved {len(employees)} employees with embeddings to 'employees_with_embeddings.json'")
