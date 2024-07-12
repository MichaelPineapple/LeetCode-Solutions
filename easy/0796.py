""" Rotate String """
class Solution(object):
    def rotateString(self, s, goal):
        for _ in range(len(s)):
            if s == goal:
                return True
            c = s[0]
            s = s[1:]+c
        return False