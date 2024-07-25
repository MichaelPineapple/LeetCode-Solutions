""" Contains Duplicate II """
# 00:04
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        m = {}
        for i, x in enumerate(nums):
            if x in m:
                j = m[x]
                if abs(i-j) <= k: return True
            m[x] = i
        return False