#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("Matrix must be a list")

    row_size = None  # Variable to store the size of the first row

    # Iterate through each row in the matrix
    for row in matrix:
        # Check if each element is a list
        if not isinstance(row, list):
            raise TypeError("Matrix must be a list of lists")

        # Check if row_size is initialized
        if row_size is None:
            row_size = len(row)  # Record the size of the first row

        # Check if each row has the same size
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        # Check if each element in the row is an integer or float
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("Matrix must contain only integers or floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be an integer")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
