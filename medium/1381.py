""" Design a Stack With Increment Operation """
# O(1)?
class CustomStack(object):

    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize
        self.m = {}

    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        i = len(self.stack) - 1
        if i < 0: return -1
        o = self.stack.pop()
        x = 0
        if i in self.m:
            x = self.m[i]
            del self.m[i]
            i -= 1
            self.m[i] = x + self.m.get(i, 0)
        o += x
        return o

    def increment(self, k, val):
        i = min(k, len(self.stack)) - 1
        self.m[i] = val + self.m.get(i, 0)