""" Product of Array Except Self """
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        l = [1] * n
        x, y = 1, 1
        for i in range(n):
            l[i] = x
            x *= nums[i]
        for i in range(n-1, -1, -1):
            l[i] *= y
            y *= nums[i]
        return l