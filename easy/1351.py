""" Count Negative Numbers in a sorted Matrix """
class Solution(object):
    def countNegatives(self, grid):
        n, m = len(grid), len(grid[0])
        p, a = 0, m
        for i in range(n):
            for j in range(a):
                x = grid[i][j]
                if x < 0:
                    a = j
                    break
                p += 1
            if a == 0: break
        return (n*m) - p