""" Permutation In String """
# O(n) Time
# O(1) Space
class Solution(object):
    def checkInclusion(self, s1, s2):
        a = ord('a')
        A, B = [0] * 26, [0] * 26
        for c in s1: A[ord(c) - a] += 1
        l, r = 0, 0
        while r < len(s2):
            crv = ord(s2[r]) - a
            if B[crv] == A[crv]:
                B[ord(s2[l]) - a] -= 1
                l += 1
            else:
                B[crv] += 1
                r += 1
                if r - l == len(s1):
                    return True
        return False