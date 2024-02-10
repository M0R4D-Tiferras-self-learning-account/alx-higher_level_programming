#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_m = []

    for row in range(len(matrix)):
        new_row = []
        for index in range(len(matrix)):
            new_row.append(matrix[row][index]**2)
        new_m.append(new_row)
    return new_m
