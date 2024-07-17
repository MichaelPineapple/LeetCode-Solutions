""" Ransom Note """
# O(n)?
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        l = [0]*26
        for c in magazine:
            l[ord(c) - ord('a')] += 1
        for c in ransomNote:
            i = ord(c) - ord('a')
            l[i] -= 1
            if l[i] < 0:
                return False
        return True