""" Largest Time for Given Digits """
class Solution(object):
    def largestTimeFromDigits(self, arr):
        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                hs, ms = str(h), str(m)
                if h < 10: hs = "0"+hs
                if m < 10: ms = "0"+ms
                s = hs+ms
                d = [0]*10
                for x in arr: d[x] += 1
                for c in s: d[int(c)] -= 1
                g = True
                for x in d:
                    if x != 0: g = False
                if g: return hs+":"+ms
        return ""