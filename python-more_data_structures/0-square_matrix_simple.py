#!/usr/bin/python3
def square(line):
    result = []

    for v in line:
        result.append(v ** 2)
    return result


def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    new_mat = map(square, matrix)
    result_mat = list(new_mat)
    return (result_mat)
