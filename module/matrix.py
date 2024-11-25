

# matrix_operations.py

def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = float(input(f"Enter value for row {i+1}, column {j+1}: "))
            row.append(val)
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

def multiply_matrices(matrix1, matrix2):
    # Check if the matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrices must have same dimensions")

    # Initialize the result matrix with zeros
    rows_matrix1 = len(matrix1)
    cols_matrix2 = len(matrix2[0])
    result = [[0] * cols_matrix2 for _ in range(rows_matrix1)]

    # Perform matrix multiplication
    for i in range(rows_matrix1):  # Iterate over rows of matrix1
        for j in range(cols_matrix2):  # Iterate over columns of matrix2
            # Calculate the dot product for result[i][j]
            for k in range(len(matrix2)):  # Iterate over columns of matrix1 / rows of matrix2
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

