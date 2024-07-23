""" String to Integer (atoi) """
class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        n = len(s)

        if n == 0: return 0

        i = 0
        z = 1
        if s[i] == '-':
            z = -1
            i += 1
        elif s[i] == '+':
            z = 1
            i += 1

        while i < n and s[i] == '0': i += 1

        a = ""
        while i < n:
            c = s[i]
            v = ord(c) - ord('0')
            if 0 <= v <= 9:
                a += c
            else:
                break
            i += 1

        if len(a) == 0: return 0
        o = int(a) * z
        u, l = ((2 ** 31) - 1), (-2 ** 31)
        if o > u: o = u
        if o < l: o = l
        return o