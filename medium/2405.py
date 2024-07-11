""" Optimal Partition of String """
# Time O(?)
# Space O(?)
class Solution(object):
    def partitionString(self, s):
        h, a = set(), 1
        for c in s:
            if c in h:
                a += 1
                h.clear()
            h.add(c)
        return a