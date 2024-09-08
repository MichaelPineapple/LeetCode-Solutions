""" Binary Search Tree Iterator """
class BSTIterator(object):

    def __init__(self, root):
        self.index = -1
        self.array = []
        def f(n):
            if not n: return
            f(n.left)
            self.array.append(n.val)
            f(n.right)
        f(root)

    def next(self):
        self.index += 1
        return self.array[self.index]

    def hasNext(self):
        return self.index < len(self.array) - 1