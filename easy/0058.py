class Solution(object):
    def lengthOfLastWord(self, s):
        x = 0
        slen = len(s)
        for i in range(slen-1, -1, -1):
            c = s[i]
            if c != ' ':
                x += 1
            elif x > 0:
                return x
        return x