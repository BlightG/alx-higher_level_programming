#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = [[x ** 2 for x in matrix[i]] for i in range(len(matrix))]
    return newmatrix
