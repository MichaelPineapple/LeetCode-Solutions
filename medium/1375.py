""" Number of Times Binary String Is Prefix Aligned """
# O(n)
class Solution(object):
    def numTimesAllBlue(self, flips):
        n = len(flips)
        s = [0]*n
        x = 0
        pp, qq = 0, -1
        for b in flips:
            i = b - 1
            s[i] = 1
            if i > qq: qq = i
            while pp < n and s[pp] == 1: pp += 1
            if pp >= qq: x += 1
        return x