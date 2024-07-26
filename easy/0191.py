""" Number of 1 Bits """
class Solution(object):
    def hammingWeight(self, n):
        o = 0
        while n > 0:
            if n % 2 == 1: o += 1
            n = n >> 1
        return o