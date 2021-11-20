matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# To show all the items
print(matrix)
print('*******************************')
# To change an individual element
matrix[0][1] = 4
print(matrix[0][1])
print(matrix)
print('*******************************')
# To show all the elements of the matrix vertically
for row in matrix:
    for item in row:
        print(item)