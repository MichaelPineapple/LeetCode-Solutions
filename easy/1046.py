""" Last Stone Weight """
class Solution(object):
    def lastStoneWeight(self, stones):
        buildHeap(stones)
        while len(stones) > 1:
            x, y = pop(stones), pop(stones)
            insert(stones, abs(x - y))
        return stones[0]


# custom heap implementation
def pop(heap):
    o = heap[0]
    j = len(heap)-1
    heap[0], heap[j] = heap[j], heap[0]
    del heap[j]
    heapify(heap, 0)
    return o

def insert(heap, v):
    def f(i):
        p = (i - 1) // 2
        if p >= 0:
            if heap[i] > heap[p]:
                heap[i], heap[p] = heap[p], heap[i]
                f(p)
    heap.append(v)
    f(len(heap)-1)

def heapify(heap, i):
    n = len(heap)
    r = (i + 1) * 2
    l = r - 1
    m = i
    if l < n and heap[l] > heap[m]: m = l
    if r < n and heap[r] > heap[m]: m = r
    if m != i:
        heap[i], heap[m] = heap[m], heap[i]
        heapify(heap, m)

def buildHeap(heap):
    n = (len(heap) // 2) - 1
    for i in range(n, -1, -1): heapify(heap, i)