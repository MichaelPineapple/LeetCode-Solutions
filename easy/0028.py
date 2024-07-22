""" Find The Index of The First Occurrence in a String """
# O(n)
class Solution(object):
    def strStr(self, haystack, needle):
        n = len(needle)
        for l in range(len(haystack) - n + 1):
            if haystack[l:l + n] == needle: return l
        return -1