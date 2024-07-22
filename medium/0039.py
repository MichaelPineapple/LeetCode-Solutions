""" Combination Sum """
# O(2^n)
class Solution(object):
    def combinationSum(self, candidates, target):
        n = len(candidates)
        o = []
        def f(s, i):
            t = sum(s)
            if t == target: o.append(s)
            if t >= target or i == n: return
            v = candidates[i]
            sl = list(s)
            sl.append(v)
            f(sl, i)
            f(s, i+1)
        f([], 0)
        return o