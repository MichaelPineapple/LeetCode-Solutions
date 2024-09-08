""" Remove Duplicates from Sorted Array II """
# O(n) Time
# O(1) Space
class Solution(object):
    def removeDuplicates(self, nums):
        p = None
        j, k = 0, 0
        for i, x in enumerate(nums):
            if x == p: j += 1
            else: j = 0
            if j < 2:
               nums[k] = x
               k += 1
            p = x
        return k