""" Maximum Number of Words Found In Sentences """
class Solution(object):
    def mostWordsFound(self, sentences):
        maxV = 0
        for s in sentences:
            l = len(s.split(' '))
            if l > maxV: maxV = l
        return maxV