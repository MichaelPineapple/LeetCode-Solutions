""" Find The Duplicate Number """
class Solution(object):
    def findDuplicate(self, nums):
        s, f = 0, 0
        while s == 0 or s != f:
            s, f = nums[s], nums[nums[f]]
        s = 0
        while s != f:
            s, f = nums[s], nums[f]
        return f