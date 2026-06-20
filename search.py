from vector_db import VectorDB

def search_disease(query):
    # Load the vector database
    vdb = VectorDB()
    results = vdb.search(query, k=3)

    # Automatically add status based on verified field
    for r in results:
        r["status"] = "Verified" if r.get("verified") else "Unverified"

    output = {
        "query": query,
        "matches": results
    }

    return output
