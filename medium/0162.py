""" Find Peak Element """
# O(log[n])
class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l+r)//2
            ml, mr = m - 1, m + 1
            mv = nums[m]
            if ml > -1 and mv < nums[ml]: r = ml
            elif mr < n and mv < nums[mr]: l = mr
            else: return m