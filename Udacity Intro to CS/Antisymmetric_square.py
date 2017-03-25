# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(grid):
    if grid == []:
        return False
    gridSize = len(grid)     # Extract size of grid  (defined by number of rows)
    numCols = len(grid[0])  # Extract number of columns
    if not (gridSize == numCols):  # If grid is non-square
        return False
    i = 0
    while i <= (gridSize - 1):
        j = 0
        while j <= (gridSize - 1):   # for each entry in ith row/column
            # work through the ith row
            if not (grid[i][j] == -grid[j][i]):
                return False
            j = j + 1
        i = i + 1   # next row/column
    return True  # Nothing was wrong.


# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False
