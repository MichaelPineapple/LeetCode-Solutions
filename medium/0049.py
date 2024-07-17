""" Group Anagrams """
# O(n*k)
class Solution(object):
    def groupAnagrams(self, strs):
        m = {}
        for a in strs:
            h = [0] * 26
            for c in a:
                h[ord(c) - 97] += 1
            k = tuple(h)
            if k not in m:
                m[k] = []
            m[k].append(a)
        return m.values()