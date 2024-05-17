import os
import random

def load_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split(", ")))
            matrix.append(row)
    return matrix


