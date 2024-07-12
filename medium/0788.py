""" Rotated Digits """
# O(n) Time
# O(1) Space
class Solution(object):
    def rotatedDigits(self, n):
        m, o = {'0': '0', '1': '1', '8': '8', '2': '5', '5': '2', '6': '9', '9': '6'}, 0
        for i in range(1, n + 1):
            r, s, v = "", str(i), True
            for c in s:
                if c in m:
                    r += m[c]
                else:
                    v = False
            if v:
                x = int(r)
                if x != i:
                    o += 1
        return o
