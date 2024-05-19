import numpy as np

def multiply_NaivLoopUnrollingFour(A, B):
    N = len(A)
    P = len(A[0])
    M = len(B[0])
    Result = np.zeros((N, M))

    if P % 4 == 0:
        for i in range(N):
            for j in range(M):
                aux = 0.0
                for k in range(0, P, 4):
                    aux += A[i][k] * B[k][j] + A[i][k + 1] * B[k + 1][j] + A[i][k + 2] * B[k + 2][j] + A[i][k + 3] * B[k + 3][j]
                Result[i][j] = aux
    elif P % 4 == 1:
        PP = P - 1
        for i in range(N):
            for j in range(M):
                aux = 0.0
                for k in range(0, PP, 4):
                    aux += A[i][k] * B[k][j] + A[i][k + 1] * B[k + 1][j] + A[i][k + 2] * B[k + 2][j] + A[i][k + 3] * B[k + 3][j]
                Result[i][j] = aux + A[i][PP] * B[PP][j]
    elif P % 4 == 2:
        PP = P - 2
        PPP = P - 1
        for i in range(N):
            for j in range(M):
                aux = 0.0
                for k in range(0, PP, 4):
                    aux += A[i][k] * B[k][j] + A[i][k + 1] * B[k + 1][j] + A[i][k + 2] * B[k + 2][j] + A[i][k + 3] * B[k + 3][j]
                Result[i][j] = aux + A[i][PP] * B[PP][j] + A[i][PPP] * B[PPP][j]
    else:
        PP = P - 3
        PPP = P - 2
        PPPP = P - 1
        for i in range(N):
            for j in range(M):
                aux = 0.0
                for k in range(0, PP, 4):
                    aux += A[i][k] * B[k][j] + A[i][k + 1] * B[k + 1][j] + A[i][k + 2] * B[k + 2][j] + A[i][k + 3] * B[k + 3][j]
                Result[i][j] = aux + A[i][PP] * B[PP][j] + A[i][PPP] * B[PPP][j] + A[i][PPPP] * B[PPPP][j]

    return Result

def printMatrix(matrix):
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()

def main():
    A = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

    B = [[17, 18, 19, 20],
        [21, 22, 23, 24],
        [25, 26, 27, 28],
        [29, 30, 31, 32]]

    C = multiply_NaivLoopUnrollingFour(A, B)
    printMatrix(C)

if __name__ == "__main__":
    main()