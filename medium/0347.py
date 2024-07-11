""" Top K Frequent Elements """
class Solution(object):
    def topKFrequent(self, nums, k):
        d, r, j = {}, [], 0
        l = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            d[n] = d.get(n, 0) + 1
        for n, v in d.items():
            l[v].append(n)
        for i in range(len(l) - 1, -1, -1):
            a = l[i]
            al = len(a)
            if al > 0:
                r.extend(a)
                j += al
            if j >= k:
                break
        return r