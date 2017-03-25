# Challenge Posted by Ashwath from forums
# Given a list of lists representing a n * n matrix as input, 
# define a  procedure that returns True if the input is an identity matrix 
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements 
# on the principal/main diagonal are 1 and all the elements outside 
# the principal diagonal are 0. 
# (A square matrix is a matrix in which the number of rows 
# is equal to the number of columns)

def is_identity_matrix(grid):
    if grid == []:
        return True
    gridSize = len(grid)     # Extract size of grid  (defined by number of rows)
    numCols = len(grid[0])  # Extract number of columns
    if not (gridSize == numCols):  # If grid is non-square
        return False
    i = 0
    while i <= (gridSize - 1):
        j = 0
        while j <= (gridSize - 1):   # for each entry in ith row/column
            # work through the ith row/column               
            if not (grid[i][j] == grid[j][i]):                
                return False
            if (i == j):
                if not (grid[i][j] == 1):
                    return False
            else:
                if not(grid[i][j] == 0):
                    return False
            j = j + 1
        i = i + 1   # next row/column
    return True  # Nothing was wrong.


# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],  
           [0,1,0,2],  
           [0,0,1,0],  
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
#>>>False           