""" Greatest Common Divisor of Strings """
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1: return ""
        n1, n2 = len(str1), len(str2)
        for i in range(min(n1, n2), 0, -1):
            if n1 % i == n2 % i == 0:
                return str1[:i]