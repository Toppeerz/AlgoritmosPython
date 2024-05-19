import os
import numpy as np
from concurrent.futures import ThreadPoolExecutor

NUM_THREADS = os.cpu_count() or 1

def main():
    A = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

    B = [[17, 18, 19, 20],
        [21, 22, 23, 24],
        [25, 26, 27, 28],
        [29, 30, 31, 32]]

    C = multiply_III4ParallelBlock(A, B, len(A), 1)
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