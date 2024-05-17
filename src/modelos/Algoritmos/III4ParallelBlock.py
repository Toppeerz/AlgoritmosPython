import os
import numpy as np
from concurrent.futures import ThreadPoolExecutor

NUM_THREADS = os.cpu_count() or 1

def main():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    C = multiply_III4ParallelBlock(A, B, 2, 1)
    print_matrix(C)

def multiply_III4ParallelBlock(A, B, size, bsize):
    C = np.zeros((size, size))

    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        executor.submit(matrix_multiply_blocks, A, B, C, size, bsize)

    return C

def matrix_multiply_blocks(A, B, C, size, bsize):
    for i1 in range(0, size, bsize):
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

if __name__ == "__main__":
    main()