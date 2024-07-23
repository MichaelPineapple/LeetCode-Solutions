""" Sum of All Odd Length Subarrays """
# O(n^2)?
# 00:07
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        o = 0
        n = len(arr)
        for l in range(n):
            for r in range(l, n, 2):
                o += sum(arr[l:r+1])
        return o