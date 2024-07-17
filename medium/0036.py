""" Valid Sudoku """
# O(1) <- Because Sudoku is always 9x9???
class Solution(object):
    def isValidSudoku(self, board):
        squareMap = {(0, 0): set(), (0, 1): set(), (0, 2): set(),
                     (1, 0): set(), (1, 1): set(), (1, 2): set(),
                     (2, 0): set(), (2, 1): set(), (2, 2): set()}
        columnLst = [set() for _ in range(9)]
        for i, row in enumerate(board):
            y = i // 3
            rowSet = set()
            for j, c in enumerate(row):
                if c != '.':
                    n = int(c)
                    x = j // 3
                    square = squareMap[(x, y)]
                    column = columnLst[j]
                    if n in square or n in rowSet or n in column:
                        return False
                    square.add(n)
                    rowSet.add(n)
                    column.add(n)
        return True
        # fuck yeah