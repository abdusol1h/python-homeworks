import numpy as np

# 1. Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)
print("Vector:", vector)

# 2. Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("3x3 Matrix:\n", matrix_3x3)

# 3. Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("Identity Matrix:\n", identity_matrix)

# 4. Create a 3x3x3 array with random values
random_3x3x3 = np.random.random((3, 3, 3))
print("3x3x3 Random Array:\n", random_3x3x3)

# 5. Create a 10x10 array with random values and find min/max values
random_10x10 = np.random.random((10, 10))
print("Min value:", np.min(random_10x10))
print("Max value:", np.max(random_10x10))

# 6. Create a random vector of size 30 and find the mean value
random_vector = np.random.random(30)
print("Mean value:", np.mean(random_vector))

# 7. Normalize a 5x5 random matrix
random_5x5 = np.random.random((5, 5))
norm_matrix = (random_5x5 - np.min(random_5x5)) / (np.max(random_5x5) - np.min(random_5x5))
print("Normalized 5x5 Matrix:\n", norm_matrix)

# 8. Multiply a 5x3 matrix by a 3x2 matrix
A = np.random.random((5, 3))
B = np.random.random((3, 2))
product_AB = np.dot(A, B)
print("5x3 * 3x2 Matrix Product:\n", product_AB)

# 9. Compute the dot product of two 3x3 matrices
M1 = np.random.random((3, 3))
M2 = np.random.random((3, 3))
dot_product = np.dot(M1, M2)
print("Dot Product of two 3x3 Matrices:\n", dot_product)

# 10. Find the transpose of a 4x4 matrix
matrix_4x4 = np.random.random((4, 4))
transpose_matrix = matrix_4x4.T
print("Transpose of 4x4 Matrix:\n", transpose_matrix)

# 11. Calculate the determinant of a 3x3 matrix
determinant = np.linalg.det(M1)
print("Determinant of a 3x3 Matrix:", determinant)

# 12. Compute the matrix product of A (3x4) and B (4x3)
A = np.random.random((3, 4))
B = np.random.random((4, 3))
matrix_product = np.dot(A, B)
print("Matrix Product A * B:\n", matrix_product)

# 13. Compute the matrix-vector product
matrix_3x3 = np.random.random((3, 3))
vector_3 = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix_3x3, vector_3)
print("Matrix-Vector Product:\n", matrix_vector_product)

# 14. Solve the linear system Ax = b
A = np.random.random((3, 3))
b = np.random.random((3, 1))
x = np.linalg.solve(A, b)
print("Solution to Ax = b:\n", x)

# 15. Find the row-wise and column-wise sums of a 5x5 matrix
matrix_5x5 = np.random.random((5, 5))
row_sums = np.sum(matrix_5x5, axis=1)
col_sums = np.sum(matrix_5x5, axis=0)
print("Row-wise sums:", row_sums)
print("Column-wise sums:", col_sums)