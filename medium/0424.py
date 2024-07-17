""" Longest Repeating Character Replacement """
# O(n)
class Solution(object):
    def characterReplacement(self, s, k):
        if len(s) < 1: return 0
        l, r, m = 0, 0, 0
        clist = [0] * 26
        while r < len(s):
            i = ord(s[r]) - ord('A')
            clist[i] += 1
            w = (r - l) + 1
            if w - max(clist) <= k:
                if w > m: m = w
                r += 1
            else:
                clist[ord(s[l]) - ord('A')] -= 1
                clist[i] -= 1
                l += 1
        return m
