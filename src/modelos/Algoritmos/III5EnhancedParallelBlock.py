import os
import numpy as np
from concurrent.futures import ThreadPoolExecutor

NUM_THREADS = os.cpu_count() or 1

def multiply_III5EnhancedParallelBlock(A, B, size, bsize):
    result = np.zeros((size, size))

    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        # First part of the matrix multiplication
        executor.submit(matrix_multiply_blocks, A, B, result, 0, size // 2, size, bsize)

        # Second part of the matrix multiplication
        executor.submit(matrix_multiply_blocks, A, B, result, size // 2, size, size, bsize)

    return result

def matrix_multiply_blocks(A, B, C, start, end, size, bsize):
    for i1 in range(start, end, bsize):
        for j1 in range(0, size, bsize):
            for k1 in range(0, size, bsize):
                for i in range(i1, min(i1 + bsize, size)):
                    for j in range(j1, min(j1 + bsize, size)):
                        for k in range(k1, min(k1 + bsize, size)):
                            C[i][j] += A[i][k] * B[k][j]

def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end=' ')
        print()

def main():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    result = multiply_III5EnhancedParallelBlock(A, B, A.shape[0], 1)

    # Print the result matrix
    print("Result Matrix:")
    print_matrix(result)

if __name__ == "__main__":
    main()