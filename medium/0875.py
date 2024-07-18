""" Koko Eating Bananas """
# O(n*Log[m])
class Solution(object):
    def minEatingSpeed(self, piles, h):
        l = sum(piles) // h
        o = r = max(piles)
        while l <= r:
            k, x = (l + r) // 2, 0
            if k == 0: break
            for b in piles: x += (b // k) + (b % k > 0)
            if x > h: l = k + 1
            else: r, o = k - 1, min(o, k)
        return o