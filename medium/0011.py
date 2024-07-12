""" Container With Most Water """
# O(n)? Time
# O(1)? Space
class Solution(object):
    def maxArea(self, height):
        n = len(height)
        mv = 0
        l, r = 0, n - 1
        while l < r:
            a, b = height[l], height[r]
            mv = max(mv, min(a, b) * (r - l))
            if a > b:
                r -= 1
            else:
                l += 1
        return mv
        # Good Job Mcl!