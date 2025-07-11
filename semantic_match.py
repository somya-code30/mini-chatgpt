from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_best_match(query, corpus):
    query_emb = model.encode(query, convert_to_tensor=True)
    corpus_emb = model.encode(corpus, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_emb, corpus_emb)
    best_index = scores.argmax().item()
    return corpus[best_index]

