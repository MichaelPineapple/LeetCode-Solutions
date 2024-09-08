""" Rotate Array """
# O(n) Time
# O(1) Space
class Solution(object):
    def rotate(self, nums, k):
        x = k % len(nums)
        nums[:] = nums[::-1]
        nums[:x] = nums[:x][::-1]
        nums[x:] = nums[x:][::-1]