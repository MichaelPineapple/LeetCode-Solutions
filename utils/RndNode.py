class RndNode:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random