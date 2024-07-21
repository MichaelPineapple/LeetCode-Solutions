""" Replace All '?' To Avoid Consecutive Repeating Characters """
class Solution(object):
    def modifyString(self, s):
        S = list(s)
        for i,c in enumerate(S):
            if c == '?':
                a = ['a', 'b', 'c']
                if i > 0:
                    l = S[i-1]
                    if l in a: a.remove(l)
                if i < len(s) - 1:
                    r = S[i+1]
                    if r in a: a.remove(r)
                c = a[0]
            S[i] = c
        return ''.join(S)