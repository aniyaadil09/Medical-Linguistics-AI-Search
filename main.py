# app/main.py
from vector_db import VectorDB

def main():
    vector_db = VectorDB()
    vector_db.load("vector.index", "metadata.pkl")
    print(f"[INFO] Loaded index (dim={vector_db.index.d}, {len(vector_db.metadata)} items)")

    while True:
        query = input("Enter a disease or symptom (or 'exit' to quit):\n> ").strip()
        if query.lower() == "exit":
            break
        results = vector_db.search(query, top_k=5)
        print("\nTop matches:")
        for res in results:
            print(f"{res}\n")

if __name__ == "__main__":
    main()
