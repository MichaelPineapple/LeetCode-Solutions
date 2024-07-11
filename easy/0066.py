class Solution(object):
    def plusOne(self, digits):
        s = ""
        for x in digits:
            s += str(x)
        val = int(s)
        val += 1
        s = str(val)
        o = []
        for c in s:
            o.append(int(c))
        return o