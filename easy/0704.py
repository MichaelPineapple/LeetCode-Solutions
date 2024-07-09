""" Binary Search """
# Time: O(?)
# Time: O(?)
class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            n = nums[m]
            if target > n:
                l = m + 1
            elif target < n:
                r = m - 1
            else:
                return m
        return -1