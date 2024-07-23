""" Repeated Substring Pattern """
class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        for i in range(2, n+1):
            if n % i == 0:
                x = n // i
                a = s[:x]
                b = a*(n // x)
                if s == b: return True
        return False