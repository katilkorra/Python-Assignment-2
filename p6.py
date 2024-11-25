from module import * 

import module.matrix as p

rows1 = int(input("Enter number of rows for Matrix 1: "))
cols1 = int(input("Enter number of columns for Matrix 1: "))
matrix1 = p.create_matrix(rows1, cols1)

rows2 = int(input("Enter number of rows for Matrix 2: "))
cols2 = int(input("Enter number of columns for Matrix 2: "))
matrix2 = p.create_matrix(rows2, cols2)

print("Matrix 1:")
for row in matrix1:
    print(row)
print("Matrix 2:")
for row in matrix2:
    print(row)

print("Matrix 1 + Matrix 2:")
result = p.add_matrices(matrix1, matrix2)
for row in result:
    print(row)

print("Matrix 1 - Matrix 2:")
result = p.subtract_matrices(matrix1, matrix2)
for row in result:
    print(row)

print("Matrix 1 * Matrix 2:")
result = p.multiply_matrices(matrix1, matrix2)
for row in result:
    print(row)


# # initialize Matrix Function Calling
# p.initializeMatrix()

# # print Matrices Function
# p.printMatrix()

# # addition Two Matrix
# p.additionMatrix()

# # multiplication of Matrix
# p.multiplicationMatrix()