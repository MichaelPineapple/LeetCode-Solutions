""" Longest Substring Without Repeating Characters """
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        z, l, m = set(), 0, 0
        for r,c in enumerate(s):
            while c in z:
                z.remove(s[l])
                l += 1
            z.add(c)
            m = max(m, (r-l)+1)
        return m