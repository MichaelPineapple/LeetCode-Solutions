""" Valid Anagram """
# O(n*log[n])
class Solution(object):
    def isAnagram(self, s, t):
        return ''.join(sorted(s)) == ''.join(sorted(t))
# ToDo - Improve Time Complexity