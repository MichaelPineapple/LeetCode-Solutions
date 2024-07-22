""" Subsets II """
# O(2^n)
class Solution(object):
    def subsetsWithDup(self, nums):
        n = len(nums)
        o = set()
        def f(s, i):
            ss = list(s)
            if i == n:
                ss.sort()
                o.add(tuple(ss))
                return
            ss.append(nums[i])
            i += 1
            f(ss, i)
            f(s, i)
        f([], 0)
        return list(o)