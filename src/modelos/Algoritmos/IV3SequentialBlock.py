def multiply_IV3SequentialBlock(matrizA, matrizB, size, bsize):
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
                            matrizC[i][k] += matrizA[i][j] * matrizB[j][k]
                            
    return matrizC
    
@staticmethod
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(element) for element in row))

if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    C = multiply_IV3SequentialBlock(A, B, 2, 128)
    print_matrix(C)