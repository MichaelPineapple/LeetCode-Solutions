""" Minimum Window Substring """
# O(n)
class Solution(object):
    def minWindow(self, s, t):
        mt, m = {}, {}
        for c in t: mt[c] = mt.get(c, 0) + 1
        g, G = 0, len(mt)
        yes = False
        win = ""
        l = 0
        for r in range(len(s)):
            rc = s[r]
            x = m[rc] = m.get(rc, 0) + 1
            if not yes:
                if x == mt.get(rc, 0):
                    g += 1
                    if g == G: yes = True
            while yes:
                sub = s[l:r+1]
                wn = len(win)
                if wn == 0 or len(sub) < wn: win = sub
                lc = s[l]
                a, b = m[lc], mt.get(lc, -1)
                if a <= b: break
                m[s[l]] -= 1
                l += 1
        return win