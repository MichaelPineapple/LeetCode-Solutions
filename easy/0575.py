""" Distribute Candies """
# Time: O(?)
# Space: O(?)
class Solution(object):
    def distributeCandies(self, candyType):
        n = len(candyType)
        h = n / 2
        s = set()
        for c in candyType:
            s.add(c)
        x = len(s)
        if x > h:
            x = h
        return x