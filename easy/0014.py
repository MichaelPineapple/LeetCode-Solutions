""" Longest Common Prefix """
class Solution(object):
    def longestCommonPrefix(self, strs):
        o, a = "", strs[0]
        for i, c in enumerate(a):
            for s in strs[1:]:
                if i == len(s) or s[i] != c: return o
            o += c
        return o