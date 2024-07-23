""" Merge Strings Alternatively """
class Solution(object):
    def mergeAlternately(self, word1, word2):
        o = ""
        n = min(len(word1), len(word2))
        for i in range(n): o += (word1[i] + word2[i])
        o += word1[n:] + word2[n:]
        return o