from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# -------- Load Transformer Model --------
# Small, fast, and accurate sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# -------- Similarity Function --------
def compute_similarity(text1, text2):
    """
    Computes semantic similarity between two texts
    using transformer embeddings + cosine similarity.
    Returns percentage score.
    """

    # Convert texts to vectors (embeddings)
    embeddings = model.encode([text1, text2])

    vec1 = embeddings[0]
    vec2 = embeddings[1]

    # Cosine similarity
    score = cosine_similarity([vec1], [vec2])[0][0]

    return round(score * 100, 2)
