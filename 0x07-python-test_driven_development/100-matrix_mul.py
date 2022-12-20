#!/usr/bin/python3
""" a function that multiplies 2 matrices """
from re import M


def _transpose(matrix):
    row = len(matrix)
    column = len(matrix[0])
    newmatrix = [[0 for j in range(row)] for i in range(column)]
    for i in range(row):
        for j in range(column):
            newmatrix[j][i] = matrix[i][j]
   

def matrix_mul(m_a, m_b):
    
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')

    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    
    if len(m_a) == 0:
        raise ValueError('m_a can\'t be empty')
  
    if len(m_b) == 0:
        raise ValueError('m_b must be a list of lists')

    for i in m_a:
        if not isinstance(i, list):
            raise TypeError('m_a must be a list of lists')
        if len(i) == 0:
            raise ValueError('m_a can\'t be empty')
        if len(i) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
        for ii in i:
            if not isinstance(ii, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
    _transpose(m_b)

    if len(m_a) != len(m_b):
        print('m_a and m_b can\'t be multiplied')
    
    if len(m_a[0]) != len(m_b[0]):
        print('m_a and m_b can\'t be multiplied')
    for j in m_b:
        if not isinstance(j, list):
            raise TypeError('m_b must be a list of lists')
        if len(j) == 0:
            raise ValueError('m_b can\'t be empty')
        if len(j) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')
        for jj in j:
            if not isinstance(jj, (int, float)):
                raise TypeError('m_b should contain only integers or floats')

    for row in range(len(m_a)):
        for column in range(len(m_b)):
            m_a[row][column] = m_a[row][column] * m_b[row][column]

    return m_a