""" Reverse Integer """
class Solution(object):
    def reverse(self, x):
        m = "2147483647"
        y = -1 if x < 0 else 1
        s = str(abs(x))[::-1]
        if len(s) == 10:
            for i, c in enumerate(s):
                a, b = int(c), int(m[i])
                if a > b: return 0
                if a < b: break
        o = int(s)
        return o*y