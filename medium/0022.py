""" Generate Parenthesis """
# O(2^n) Time
# O(n) Space
class Solution(object):
    def generateParenthesis(self, n):
        self.num, self.valid = n, []
        self.f(0, 0, "")
        return self.valid

    def f(self, o, c, s):
        if o == c == self.num: self.valid.append(s)
        if o > c: self.f(o, c + 1, s + ")")
        if o < self.num: self.f(o + 1, c, s + "(")