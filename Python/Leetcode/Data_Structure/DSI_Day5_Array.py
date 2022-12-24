import collections
import itertools


'''36. Valid Sudoku'''

def isValidSudoku(self, board):
    N = 9

    # Use hash set to record the status
    rows = [set() for _ in range(N)]
    cols = [set() for _ in range(N)]
    boxes = [set() for _ in range(N)]

    for r in range(N):
        for c in range(N):
            val = board[r][c]
            # Check if the position is filled with number
            if val == ".":
                continue

            # Check the row
            if val in rows[r]:
                return False
            rows[r].add(val)

            # Check the column
            if val in cols[c]:
                return False
            cols[c].add(val)

            # Check the box
            idx = (r // 3) * 3 + c // 3
            if val in boxes[idx]:
                return False
            boxes[idx].add(val)

    return True


'''74. Search a 2D Matrix'''

def searchMatrix(matrix, target):
    
    m = len(matrix)

    for i in range(m):
        if target in matrix[i] :
            return True

    return False


