""" H-Index """
# O(n*log[n])
class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        n = len(citations)
        h = 0
        for i in range(n): h = max(h, min(n-i, citations[i]))
        return h