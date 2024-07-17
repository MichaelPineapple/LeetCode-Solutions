""" Min Stack """
# O(1)
class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        m = self.getMin()
        if m is None: m = val
        else: m = min(val, m)
        self.stack.append([val, m])

    def pop(self):
        self.stack.pop()

    def top(self):
        n = len(self.stack)
        if n > 0: return self.stack[n - 1][0]
        return None

    def getMin(self):
        n = len(self.stack)
        if n > 0: return self.stack[n - 1][1]
        return None