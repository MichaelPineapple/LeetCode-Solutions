""" Search Insert Position """
# o(log[n])
class Solution(object):
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            v = nums[m]
            if v > target: r = m - 1
            elif v < target: l = m + 1
            else: return m
        return r + 1