""" Sort Array by Increasing Frequency """
# 00:11
class Solution(object):
    def frequencySort(self, nums):
        o, m = [], {}
        for x in nums: m[x] = m.get(x, 0) + 1
        a = m.items()
        a.sort(key=lambda y: (y[1], -y[0]))
        for x,n in a: o.extend([x]*n)
        return o