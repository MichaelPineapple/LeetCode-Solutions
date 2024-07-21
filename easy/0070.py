""" Climbing Stairs """
# O(n)
class Solution(object):
    def climbStairs(self, n):
        memo = {n: 1, n + 1: 0}
        def f(i):
            if i in memo: return memo[i]
            x = f(i + 1) + f(i + 2)
            memo[i] = x
            return x
        return f(0)
