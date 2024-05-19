import numpy as np
from .WinogradOriginal import winograd_original_multiply

def norm_inf(matrix, rows, cols):
    max_val = -np.inf
    for i in range(rows):
        for j in range(cols):
            max_val = max(max_val, abs(matrix[i][j]))
    return max_val

def multiply_with_scalar(source, rows, cols, scalar):
    target = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            target[i][j] = source[i][j] * scalar
    return target

def multiply_WinogradScaled(A, B, N, P, M):
    # Crear copias escaladas de A y B
    CopyA = np.zeros((N, P))
    CopyB = np.zeros((P, M))
    
    # Factores de escalamiento
    a = norm_inf(A, N, P)
    b = norm_inf(B, P, M)
    lambda_ = np.floor(0.5 + np.log(b / a) / np.log(4))
    
    # Escalamiento
    CopyA = multiply_with_scalar(A, N, P, np.power(2, lambda_))
    CopyB = multiply_with_scalar(B, P, M, np.power(2, -lambda_))
    
    # Usando Winograd con matrices escaladas
    Result = winograd_original_multiply(CopyA, CopyB, N, P, M)
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

    Result = multiply_WinogradScaled(A, B, 4, 4, 4)
    print_matrix(Result)
