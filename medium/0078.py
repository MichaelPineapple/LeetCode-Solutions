""" Subsets """
# O(2^n)
class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        o = []
        def f(s, i):
            if i == n:
                o.append(s)
                return
            v = nums[i]
            s2 = list(s)
            s2.append(v)
            i += 1
            f(s2, i)
            f(s, i)
        f([], 0)
        return o