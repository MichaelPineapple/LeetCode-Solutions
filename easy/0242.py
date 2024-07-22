""" Valid Anagram """
# O(n)
class Solution(object):
    def isAnagram(self, s, t):
        a = [0]*26
        for c in s: a[ord(c) - ord('a')] += 1
        for c in t: a[ord(c) - ord('a')] -= 1
        for x in a:
            if x != 0: return False
        return True