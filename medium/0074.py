""" Search a 2D Matrix """
# O(log(m*n))?
class Solution(object):
    def searchMatrix(self, matrix, target):
        w = len(matrix[0])
        for i, row in enumerate(matrix):
            first = row[0]
            if target < first:
                break
            last = row[w-1]
            if target > last:
                continue
            l, r = 0, w - 1
            while l <= r:
                m = (l+r)//2
                x = row[m]
                if target > x:
                    l = m + 1
                elif target < x:
                    r = m - 1
                else:
                    return True
        return False
        # Hell yeah