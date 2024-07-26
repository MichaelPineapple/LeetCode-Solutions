""" Reverse Bits """
class Solution:
    def reverseBits(self, n):
        o = 0
        for i in range(32):
            b = (n >> i) & 1
            o = o | (b << (31 - i))
        return o