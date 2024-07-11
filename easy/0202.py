class Solution(object):
    def isHappy(self, n):
        q = set()
        while n != 1:
            if n in q:
                return False
            q.add(n)
            s = str(n)
            t = 0
            for c in s:
                x = int(c)
                t += (x * x)
            n = t
        return True