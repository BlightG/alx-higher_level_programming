#!/usr/bin/python3

def matrix_divided(matrix, div):
    newmatrix = matrix.copy()
    
    for i in range(len(matrix)):
        newmatrix[i] = matrix[i].copy()
        
    
    
    for i in range(len(newmatrix)):
        for j in range(len(newmatrix[i])):
            newmatrix[i][j] = round(newmatrix[i][j] / div, 2)


    return newmatrix