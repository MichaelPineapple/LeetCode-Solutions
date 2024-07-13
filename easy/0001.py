""" Two Sum """
class Solution(object):
    def twoSum(self, nums, target):
        m = {}
        for i, n in enumerate(nums):
            k = target - n
            if k in m:
                return [i, m[k]]
            m[n] = i