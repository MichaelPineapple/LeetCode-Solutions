""" Best Time To Buy And Sell Stock """
# Time: O(?)
# Space: O(?)
class Solution(object):
    def maxProfit(self, prices):
        l, r, m = 0, 1, 0
        while r < len(prices):
            b, s = prices[l], prices[r]
            if b < s:
                m = max(m, s - b)
            else:
                l = r
            r += 1
        return m