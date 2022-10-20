#!/usr/bin/python3
"""A module for returning a new 2d list made from dividing every element of
a 2d an user input int type variable
"""


def matrix_divided(matrix, div):
    """ a function to divide each element of a matrix by an int ዶክ ቴስት

        Args:
            matix (2d-list): a list of list containing only int and float type
            div (int): an int or float type

        Returns:
            list: raises an exception or returns a new 2d list

    """
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if isinstance(matrix, list):
        lenght = len(matrix[0])
        for i in matrix:
            if not isinstance(i, list):
                raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')

            elif lenght != len(i):
                raise TypeError('Each row of the matrix must have \
the same size')

            for num in i:
                if not isinstance(num, (int, float)):
                    raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')

                if num == 0:
                    raise ZeroDivisionError('division by zero')

    newmatrix = matrix.copy()

    for i in range(len(matrix)):
        newmatrix[i] = matrix[i].copy()

    for i in range(len(newmatrix)):
        for j in range(len(newmatrix[i])):
            newmatrix[i][j] = round(newmatrix[i][j] / div, 2)

    return newmatrix
