""" Reverse Words in a String """
class Solution(object):
    def reverseWords(self, s):
        s = s.strip()
        words = s.split(' ')[::-1]
        o = ""
        for w in words:
            if len(w.strip()) > 0:
                o += (w + " ")
        return o.strip()