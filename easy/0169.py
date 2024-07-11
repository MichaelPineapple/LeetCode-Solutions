class Solution(object):
    def majorityElement(self, nums):
        d, m, a = {}, 0, 0
        for x in nums:
            n = d.get(x, 0) + 1
            d[x] = n
            if n > m:
                m = n
                a = x
        return a