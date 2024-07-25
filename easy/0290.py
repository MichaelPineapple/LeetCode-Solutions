""" Word Pattern """
class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split(' ')
        if len(pattern) != len(words): return False
        wMap, cMap = {}, {}
        for i, w in enumerate(words):
            c = pattern[i]
            if w not in wMap and c not in cMap: wMap[w], cMap[c] = c, w
            if wMap.get(w, None) != c or cMap.get(c, None) != w: return False
        return True