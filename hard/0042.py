""" Trapping Rain Water """
# O(n)
class Solution(object):
    def trap(self, height):
        W, H1, H2, j = 0, 0, 0, 0
        for i, h in enumerate(height):
            if h > H1: H1, j = h, i
            W += (H1 - h)
        for i in range(len(height)-1, j-1, -1):
            h = height[i]
            if h > H2: H2 = h
            W -= (H1 - h)
            W += (H2 - h)
        return W