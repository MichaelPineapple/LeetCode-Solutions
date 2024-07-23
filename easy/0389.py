""" Find the Difference """
class Solution(object):
    def findTheDifference(self, s, t):
        s += "{"
        l, a = [0]*27, ord('a')
        for i in range(len(s)):
            l[ord(s[i])-a] += 1
            l[ord(t[i])-a] -= 1
        return chr(l.index(-1)+a)