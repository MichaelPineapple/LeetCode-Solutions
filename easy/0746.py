""" Min Cost Cimbing Stairs """
# O(n)
class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        memo = {n:0, n+1:0}
        def f(i):
            if i in memo: return memo[i]
            c = cost[i] if i >= 0 else 0
            a = f(i+1)
            b = f(i+2)
            x = min(a, b) + c
            memo[i] = x
            return x
        return f(-1)