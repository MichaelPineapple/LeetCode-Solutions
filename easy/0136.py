""" Single Number """
class Solution(object):
    def singleNumber(self, nums):
        s = set()
        for x in nums:
            if x in s: s.remove(x)
            else: s.add(x)
        return s.pop()