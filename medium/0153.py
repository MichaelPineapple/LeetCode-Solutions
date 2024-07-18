""" Find Minimum In Rotated Sorted Array """
# O(log[n])
class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l <= r:
            lv, rv = nums[l], nums[r]
            if (r - l) <= 1: return min(lv, rv)
            m = (l + r) // 2
            mv = nums[m]
            if lv > mv: r = m
            elif rv < mv: l = m
            else: return lv