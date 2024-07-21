""" Remove Duplicates From Sorted Array """
class Solution(object):
    def removeDuplicates(self, nums):
        i, k, p = 0, 0, nums[0]-1
        while i < len(nums):
            x = nums[i]
            if x == p:
                del nums[i]
            else:
                p = x
                k += 1
                i += 1
        return k