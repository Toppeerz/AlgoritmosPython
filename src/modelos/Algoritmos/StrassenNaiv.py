import numpy as np

def multiply_StrassenNaiv(A, B):
    N = len(A)
    P = len(A[0])
    M = len(B[0])
    MaxSize = max(N, max(P, M))
    if MaxSize < 16:
        MaxSize = 16
    
    k = int(np.floor(np.log(MaxSize) / np.log(2)) - 4)
    m = int(np.floor(MaxSize * 2**-k) + 1)
    NewSize = m * int(2**k)
    
    NewA = np.zeros((NewSize, NewSize))
    NewB = np.zeros((NewSize, NewSize))
    AuxResult = np.zeros((NewSize, NewSize))
    
    NewA[:N, :P] = A
    NewB[:P, :M] = B
    
    StrassenNaivStep(NewA, NewB, AuxResult, NewSize, m)
    
    Result = AuxResult[:N, :M]
    return Result

def StrassenNaivStep(A, B, Result, N, m):
    if N % 2 == 0 and N > m:
        NewSize = N // 2
        
        A11, A12, A21, A22 = split_matrix(A, NewSize)
        B11, B12, B21, B22 = split_matrix(B, NewSize)
        
        ResultPart11 = np.zeros((NewSize, NewSize))
        ResultPart12 = np.zeros((NewSize, NewSize))
        ResultPart21 = np.zeros((NewSize, NewSize))
        ResultPart22 = np.zeros((NewSize, NewSize))
        
        Helper1 = np.zeros((NewSize, NewSize))
        Helper2 = np.zeros((NewSize, NewSize))
        
        Aux1 = np.zeros((NewSize, NewSize))
        Aux2 = np.zeros((NewSize, NewSize))
        Aux3 = np.zeros((NewSize, NewSize))
        Aux4 = np.zeros((NewSize, NewSize))
        Aux5 = np.zeros((NewSize, NewSize))
        Aux6 = np.zeros((NewSize, NewSize))
        Aux7 = np.zeros((NewSize, NewSize))
        
        Plus(A11, A22, Helper1)
        Plus(B11, B22, Helper2)
        StrassenNaivStep(Helper1, Helper2, Aux1, NewSize, m)
        
        Plus(A21, A22, Helper1)
        StrassenNaivStep(Helper1, B11, Aux2, NewSize, m)
        
        Minus(B12, B22, Helper1)
        StrassenNaivStep(A11, Helper1, Aux3, NewSize, m)
        
        Minus(B21, B11, Helper1)
        StrassenNaivStep(A22, Helper1, Aux4, NewSize, m)
        
        Plus(A11, A12, Helper1)
        StrassenNaivStep(Helper1, B22, Aux5, NewSize, m)
        
        Minus(A21, A11, Helper1)
        Plus(B11, B12, Helper2)
        StrassenNaivStep(Helper1, Helper2, Aux6, NewSize, m)
        
        Minus(A12, A22, Helper1)
        Plus(B21, B22, Helper2)
        StrassenNaivStep(Helper1, Helper2, Aux7, NewSize, m)
        
        Plus(Aux1, Aux4, ResultPart11)
        Minus(ResultPart11, Aux5, ResultPart11)
        Plus(ResultPart11, Aux7, ResultPart11)
        
        Plus(Aux3, Aux5, ResultPart12)
        
        Plus(Aux2, Aux4, ResultPart21)
        
        Plus(Aux1, Aux3, ResultPart22)
        Minus(ResultPart22, Aux2, ResultPart22)
        Plus(ResultPart22, Aux6, ResultPart22)
        
        combine_submatrices(Result, ResultPart11, ResultPart12, ResultPart21, ResultPart22, NewSize)
    else:
        NaivStandard(A, B, Result)

def NaivStandard(A, B, Result):
    N = len(A)
    P = len(A[0])
    M = len(B[0])
    for i in range(N):
        for j in range(M):
            aux = 0.0
            for k in range(P):
                aux += A[i][k] * B[k][j]
            Result[i][j] = aux

def Plus(A, B, Result):
    N = len(A)
    M = len(A[0])
    for i in range(N):
        for j in range(M):
            Result[i][j] = A[i][j] + B[i][j]

def Minus(A, B, Result):
    N = len(A)
    M = len(A[0])
    for i in range(N):
        for j in range(M):
            Result[i][j] = A[i][j] - B[i][j]

def split_matrix(A, size):
    A11 = A[:size, :size]
    A12 = A[:size, size:]
    A21 = A[size:, :size]
    A22 = A[size:, size:]
    return A11, A12, A21, A22

def combine_submatrices(Result, C11, C12, C21, C22, size):
    Result[:size, :size] = C11
    Result[:size, size:] = C12
    Result[size:, :size] = C21
    Result[size:, size:] = C22

def printMatrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    C = multiply_StrassenNaiv(A, B)
    printMatrix(C)