""" Rank Transform of An Array """
class Solution(object):
    def arrayRankTransform(self, arr):
        out = []
        arr2 = [x for x in arr]
        arr2.sort()
        ranks = {}
        r = 0
        p = None
        for x in arr2:
            if x != p:
                r += 1
                ranks[x] = r
            p = x

        for x in arr:
            a = ranks[x]
            out.append(a)

        return out