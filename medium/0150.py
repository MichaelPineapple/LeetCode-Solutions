""" Evaluate Reverse Polish Notation """
# O(n)
class Solution(object):
    def evalRPN(self, tokens):
        fmap = {
            "+": lambda x, y: y + x,
            "*": lambda x, y: y * x,
            "-": lambda x, y: y - x,
            "/": lambda x, y: float(y) / float(x),
        }
        stack = []
        for t in tokens:
            if t in fmap: t = fmap[t](stack.pop(), stack.pop())
            stack.append(int(t))
        return stack.pop()