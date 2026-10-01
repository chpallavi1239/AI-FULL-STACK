from sentence_transformers import SentenceTransformer

with open("fest_info.text", "r", encoding="utf-8") as f:
    text = f.read()

print(f"Your file has {len(text)} characters.")
print()
print("Sample text:", text[:300])
def chunk_text(text, chunk_size = 300, overlap = 50):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap
    return chunks 

chunks = chunk_text(text)

model = SentenceTransformer('all-minim-L6-V2')
embeddings = model.encode(chunks)

print(f"{len(chunks)}created -> shape of embeddings:{embeddings.shape})")
 
for i in range(len(chunks)):
    print(f"chunk_{i+1}: {chunks[i]}")
    print()
    print("------------------------------")


