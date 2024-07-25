""" Move Zeros """
class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i, x in enumerate(nums):
            if x != 0:
                nums[j] = x
                j += 1
        nums[j:] = [0]*(len(nums)-j)