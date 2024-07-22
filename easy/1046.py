from utils import MaxHeap

""" Last Stone Weight """
class Solution(object):
    def lastStoneWeight(self, stones):
        MaxHeap.build(stones)
        while len(stones) > 1:
            x, y = MaxHeap.pop(stones), MaxHeap.pop(stones)
            MaxHeap.push(stones, abs(x - y))
        return stones[0]