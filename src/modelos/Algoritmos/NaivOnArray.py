import numpy as np

def multiply_NaivOnArray(A, B):
    N = len(A)
    P = len(A[0])
    M = len(B[0])
    Result = np.zeros((N, M))

    for i in range(N):
        for j in range(M):
            Result[i][j] = 0.0
            for k in range(P):
                Result[i][j] += A[i][k] * B[k][j]

    return Result

def printMatrix(matrix):
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()

def main():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    C = multiply_NaivOnArray(A, B)
    printMatrix(C)

if __name__ == "__main__":
    main()