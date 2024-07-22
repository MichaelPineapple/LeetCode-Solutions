""" Permutations """
# O(n!)
class Solution(object):
    def permute(self, nums):
        n = len(nums)
        o = []
        def f(s, a):
            if len(s) == n: o.append(s)
            for x in a:
                b, c = set(a), list(s)
                b.remove(x), c.append(x)
                f(c, b)
        f([], set(nums))
        return o