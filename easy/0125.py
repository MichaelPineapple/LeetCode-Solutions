""" Valid Palindrome """
class Solution(object):
    def isPalindrome(self, s):
        n = len(s)
        h = n / 2
        j = n - 1
        for c in s:
            if j < h:
                break
            if c.isalnum():
                c2 = s[j]
                while not c2.isalnum():
                    j = j - 1
                    c2 = s[j]
                if c2.lower() != c.lower():
                    return False
                j = j - 1
        return True