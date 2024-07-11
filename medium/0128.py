""" Longest Consecutive Sequence """
class Solution(object):
    def longestConsecutive(self, nums):
        m, mx = set(nums), 0
        for n in nums:
            if n - 1 not in m:
                x = n + 1
                while x in m:
                    x += 1
                mx = max(mx, x-n)
        return mx