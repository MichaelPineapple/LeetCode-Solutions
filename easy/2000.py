""" Reverse Prefix of Word """
class Solution(object):
    def reversePrefix(self, word, ch):
        foi = -1
        for i in range(len(word)):
            c = word[i]
            if c == ch:
                foi = i
                break
        foi += 1
        s, r = word[:foi], ""
        for i in range(len(s) - 1, -1, -1): r += s[i]
        return r + word[foi:]
