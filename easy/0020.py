""" Valid Parenthesis """
class Solution(object):
    def isValid(self, s):
        stack, m = [], {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif c in [')', ']', '}']:
                if len(stack) == 0 or c != m[stack.pop()]:
                    return False
        return len(stack) == 0