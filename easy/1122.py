""" Relative Sort Array """
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        l, m = [], {}
        a2l = len(arr2)
        for i in range(a2l):
            m[arr2[i]] = i
            l.append(0)

        q = []
        for x in arr1:
            if x in m:
                i = m[x]
                l[i] += 1
            else:
                q.append(x)
        q.sort()

        r = []
        for i in range(a2l):
            v = arr2[i]
            for _ in range(l[i]):
                r.append(v)
        r.extend(q)

        return r