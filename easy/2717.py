""" Semi-Ordered Permutation """
class Solution(object):
    def semiOrderedPermutation(self, nums):
        n = len(nums)
        i, j = None, None
        for k, x in enumerate(nums):
            if i is None and x == 1: i = k
            if j is None and x == n: j = k
        o = i + ((n - 1) - j)
        if j - i < 0: o -= 1
        return o