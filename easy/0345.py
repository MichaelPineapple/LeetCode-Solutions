""" Reverse Vowel of a String """
class Solution(object):
    def reverseVowels(self, s):
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        vowelArray, indexArray, strArray = [], [], list(s)
        for i, c in enumerate(s):
            if c in vowels:
                vowelArray.append(c)
                indexArray.append(i)
        vowelArray = vowelArray[::-1]
        for i, j in enumerate(indexArray): strArray[j] = vowelArray[i]
        return ''.join(strArray)