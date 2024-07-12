""" Roman To Integer """
# O(n) Time
# O(1) Space
class Solution(object):
    def romanToInt(self, s):
        m = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        m2 = {'I':('V', 'X'), 'X':('L', 'C'), 'C':('D', 'M')}
        t = 0
        for i, c in enumerate(s):
            v = m[c]
            q = m2.get(c, ())
            if i < len(s) - 1 and s[i+1] in q:
                t -= v
            else:
                t += v
        return t
