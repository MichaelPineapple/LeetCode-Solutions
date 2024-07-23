""" Set Matrix Zeros """
class Solution(object):
    def setZeroes(self, matrix):
        zeroRows, zeroCols = set(), set()
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == 0: zeroRows.add(i), zeroCols.add(j)
        for i, row in enumerate(matrix):
            for j in range(len(row)):
                if j in zeroCols or i in zeroRows: row[j] = 0