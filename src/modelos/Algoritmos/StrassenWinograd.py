import numpy as np

def multiply_StrassenWinograd(A, B, N, P, M):
    MaxSize = max(N, P, M)

    if MaxSize < 16:
        MaxSize = 16  # otherwise it is not possible to compute k

    k = int(np.floor(np.log2(MaxSize)) - 4)
    m = int(np.floor(MaxSize * 2**(-k)) + 1)
    NewSize = m * int(2**k)

    # add zero rows and columns to use Strassen's algorithm
    NewA = np.zeros((NewSize, NewSize))
    NewB = np.zeros((NewSize, NewSize))
    AuxResult = np.zeros((NewSize, NewSize))

    # Copy values from A and B
    NewA[:N, :P] = A
    NewB[:P, :M] = B

    strassen_winograd_step(NewA, NewB, AuxResult, NewSize, m)

    # Extract the result
    Result = AuxResult[:N, :M]
    return Result

def strassen_winograd_step(A, B, Result, N, m):
    if (N % 2 == 0) and (N > m):  # recursive use of strassen_winograd_step
        NewSize = N // 2

        # Decompose A and B
        A11, A12 = A[:NewSize, :NewSize], A[:NewSize, NewSize:]
        A21, A22 = A[NewSize:, :NewSize], A[NewSize:, NewSize:]
        B11, B12 = B[:NewSize, :NewSize], B[:NewSize, NewSize:]
        B21, B22 = B[NewSize:, :NewSize], B[NewSize:, NewSize:]

        # Create ResultPart, Aux1,...,Aux7 and Helper1, Helper2
        A1 = np.zeros((NewSize, NewSize))
        A2 = np.zeros((NewSize, NewSize))
        B1 = np.zeros((NewSize, NewSize))
        B2 = np.zeros((NewSize, NewSize))
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
        Aux8 = np.zeros((NewSize, NewSize))
        Aux9 = np.zeros((NewSize, NewSize))

        # Computing the 4 + 9 auxiliary variables
        minus(A11, A21, A1, NewSize, NewSize)
        minus(A22, A1, A2, NewSize, NewSize)
        minus(B22, B12, B1, NewSize, NewSize)
        plus(B1, B11, B2, NewSize, NewSize)
        strassen_winograd_step(A11, B11, Aux1, NewSize, m)
        strassen_winograd_step(A12, B21, Aux2, NewSize, m)
        strassen_winograd_step(A2, B2, Aux3, NewSize, m)
        plus(A21, A22, Helper1, NewSize, NewSize)
        minus(B12, B11, Helper2, NewSize, NewSize)
        strassen_winograd_step(Helper1, Helper2, Aux4, NewSize, m)
        strassen_winograd_step(A1, B1, Aux5, NewSize, m)
        minus(A12, A2, Helper1, NewSize, NewSize)
        strassen_winograd_step(Helper1, B22, Aux6, NewSize, m)
        minus(B21, B2, Helper1, NewSize, NewSize)
        strassen_winograd_step(A22, Helper1, Aux7, NewSize, m)
        plus(Aux1, Aux3, Aux8, NewSize, NewSize)
        plus(Aux8, Aux4, Aux9, NewSize, NewSize)

        # Computing the four parts of the result
        plus(Aux1, Aux2, ResultPart11, NewSize, NewSize)
        plus(Aux9, Aux6, ResultPart12, NewSize, NewSize)
        plus(Aux8, Aux5, Helper1, NewSize, NewSize)
        plus(Helper1, Aux7, ResultPart21, NewSize, NewSize)
        plus(Aux9, Aux5, ResultPart22, NewSize, NewSize)

        # Store results in the "result matrix"
        Result[:NewSize, :NewSize] = ResultPart11
        Result[:NewSize, NewSize:] = ResultPart12
        Result[NewSize:, :NewSize] = ResultPart21
        Result[NewSize:, NewSize:] = ResultPart22
    else:
        # Use naive algorithm
        naiv_standard(A, B, Result, N, N, N)

def plus(A, B, Result, N, M):
    for i in range(N):
        for j in range(M):
            Result[i][j] = A[i][j] + B[i][j]

def minus(A, B, Result, N, M):
    for i in range(N):
        for j in range(M):
            Result[i][j] = A[i][j] - B[i][j]

def naiv_standard(A, B, Result, N, P, M):
    for i in range(N):
        for j in range(M):
            aux = 0.0
            for k in range(P):
                aux += A[i][k] * B[k][j]
            Result[i][j] = aux

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    # Example usage
    A = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

    B = [[17, 18, 19, 20],
        [21, 22, 23, 24],
        [25, 26, 27, 28],
        [29, 30, 31, 32]]
    Result = np.zeros((4, 4))

    Result = multiply_StrassenWinograd(A, B, 4, 4, 4)

    # Print the result
    print_matrix(Result)
