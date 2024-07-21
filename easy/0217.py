""" Contains Duplicate """
class Solution(object):
    def containsDuplicate(self, nums):
        l = set()
        for i in nums:
            if i in l:
                return True
            l.add(i)
        return False