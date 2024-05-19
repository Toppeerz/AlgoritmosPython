def multiply_III3SequentialBlock(matrizA, matrizB, size, bsize):
    """
    Realiza la multiplicación de matrices utilizando el algoritmo III3SequentialBlock.

    Args:
        matrizA (list): Matriz A.
        matrizB (list): Matriz B.
        matrizC (list): Matriz C, donde se almacenará el resultado.
        size (int): Tamaño de las matrices.
        bsize (int): Tamaño del bloque.

    Returns:
        None
    """
    matrizC = [[0 for _ in range(size)] for _ in range(size)]
    for i1 in range(0, size, bsize):
        for j1 in range(0, size, bsize):
            for k1 in range(0, size, bsize):
                for i in range(i1, min(i1 + bsize, size)):
                    for j in range(j1, min(j1 + bsize, size)):
                        for k in range(k1, min(k1 + bsize, size)):
                            matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
                            
    return matrizC

@staticmethod
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(element) for element in row))

if __name__ == "__main__":
    A = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

    B = [[17, 18, 19, 20],
        [21, 22, 23, 24],
        [25, 26, 27, 28],
        [29, 30, 31, 32]]

    C = multiply_III3SequentialBlock(A, B, 4, 1)
    print_matrix(C)
