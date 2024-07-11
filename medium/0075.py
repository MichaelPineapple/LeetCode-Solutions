""" Sort Colors """
# Time:     O(n)
# Space:    O(1)
class Solution(object):
    def sortColors(self, nums):
        l = [0] * 3
        for x in nums:
            l[x] += 1
        i = 0
        for j in range(3):
            for _ in range(l[j]):
                nums[i] = j
                i += 1
