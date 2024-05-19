import numpy as np

def winograd_original_multiply(A, B, N, P, M):
    upsilon = P % 2
    gamma = P - upsilon
    y = np.zeros(M)
    z = np.zeros(N)
    Result = np.zeros((M, N))

    for i in range(M):
        aux = 0
        for j in range(0, gamma, 2):
            aux += A[i][j] * A[i][j + 1]
        y[i] = aux

    for i in range(N):
        aux = 0
        for j in range(0, gamma, 2):
            aux += B[j][i] * B[j + 1][i]
        z[i] = aux

    if upsilon == 1:
        PP = P - 1
        for i in range(M):
            for k in range(N):
                aux = 0
                for j in range(0, gamma, 2):
                    aux += (A[i][j] + B[j + 1][k]) * (A[i][j + 1] + B[j][k])
                Result[i][k] = aux - y[i] - z[k] + A[i][PP] * B[PP][k]
    else:
        for i in range(M):
            for k in range(N):
                aux = 0
                for j in range(0, gamma, 2):
                    aux += (A[i][j] + B[j + 1][k]) * (A[i][j + 1] + B[j][k])
                Result[i][k] = aux - y[i] - z[k]

    return Result

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    A = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

    B = [[17, 18, 19, 20],
        [21, 22, 23, 24],
        [25, 26, 27, 28],
        [29, 30, 31, 32]]

    Result = winograd_original_multiply(A, B, 4, 4, 4)
    print_matrix(Result)
