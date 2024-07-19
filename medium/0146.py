""" LRU Cache """
# O(1)

class LruNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        self.queueMap = {}
        self.head = node = LruNode(None, None)
        for i in range(capacity):
            key = -(i+1)
            new = LruNode(None, key)
            self.queueMap[key] = new
            node.next = new
            new.prev = node
            node = new
        self.head = self.head.next
        self.tail = node

    def get(self, key):
        if key not in self.queueMap: return -1
        node = self.queueMap[key]
        self.moveToFront(node)
        return node.val

    def moveToFront(self, node):
        if node == self.head: return
        left = node.prev
        right = node.next
        if node == self.tail: self.tail = left
        if left: left.next = right
        if right: right.prev = left
        node.next = self.head
        self.head.prev = node
        self.head = node

    def put(self, key, value):
        node = self.queueMap.get(key, self.tail)
        del self.queueMap[node.key]
        self.queueMap[key] = node
        node.val, node.key = value, key
        self.moveToFront(node)