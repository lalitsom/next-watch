import numpy as np
import faiss

# Step 1: Create random vectors
dimension = 64  # Dimension of vectors
num_vectors = 1000  # Number of vectors in the dataset
query_vectors = 5   # Number of query vectors

# Generate random dataset and query vectors
data = np.random.random((num_vectors, dimension)).astype('float32')
queries = np.random.random((query_vectors, dimension)).astype('float32')

# Step 2: Build FAISS Index
index = faiss.IndexFlatL2(dimension)  # L2 norm (Euclidean distance)
print(f"Is the index trained? {index.is_trained}")

# Add data to the index
index.add(data)
print(f"Number of vectors in the index: {index.ntotal}")

# Step 3: Perform a search
k = 3  # Number of nearest neighbors
distances, indices = index.search(queries, k)

# Step 4: Print Results
print("Query Results:")
for i in range(len(queries)):
    print(f"Query {i + 1}:")
    for j in range(k):
        print(f"  Neighbor {j + 1}: Index={indices[i][j]}, Distance={distances[i][j]:.4f}")
