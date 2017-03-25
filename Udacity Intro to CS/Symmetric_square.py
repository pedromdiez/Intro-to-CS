# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(grid):
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
            # work through the ith row
            if not (grid[i][j] == grid[j][i]):
                return False
            j = j + 1
        i = i + 1   # next row/column
    return True  # Nothing was wrong.


#print symmetric([[1, 2, 3],
#                [2, 3, 4],
#                [3, 4, 1]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "fish"],
#                ["fish", "fish", "cat"]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "dog"],
#                ["fish","fish","cat"]])
#>>> False

#print symmetric([[1, 2],
#                [2, 1]])
#>>> True

#print symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]])
#>>> False

#print symmetric([[1,2,3],
#                 [2,3,1]])
#>>> False