""" Count And Say """
# O(2^n) <-- Optimal
class Solution(object):
    def countAndSay(self, n):
        if n == 1: return "1"
        return rle(self.countAndSay(n - 1))

def rle(s):
    s += ";"
    o, p, x = "", ';', 0
    for c in s:
        if c != p:
            o += str(x) + str(p)
            x = 0
        x += 1
        p = c
    return o[2:]