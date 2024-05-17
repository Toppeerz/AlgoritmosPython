import numpy as np

def multiply_NaivLoopUnrollingTwo(A, B):
    N = len(A)
    P = len(A[0])
    M = len(B[0])
    Result = np.zeros((N, M))

    if P % 2 == 0:
        for i in range(N):
            for j in range(M):
                aux = 0.0
                for k in range(0, P, 2):
                    aux += A[i][k] * B[k][j] + A[i][k + 1] * B[k + 1][j]
                Result[i][j] = aux
    else:
        PP = P - 1
        for i in range(N):
            for j in range(M):
                aux = 0.0
                for k in range(0, PP, 2):
                    aux += A[i][k] * B[k][j] + A[i][k + 1] * B[k + 1][j]
                Result[i][j] = aux + A[i][PP] * B[PP][j]

    return Result

def printMatrix(matrix):
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()

def main():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    C = multiply(A, B)
    printMatrix(C)

if __name__ == "__main__":
    main()