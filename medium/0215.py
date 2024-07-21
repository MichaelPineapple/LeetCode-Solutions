""" Kth Largest Element In An Array """
# O(n*log[n]) <-- just as good as sorting SMH
class Solution(object):
    def findKthLargest(self, nums, k):
        heap = MclHeap(nums)
        o = None
        for _ in range(k): o = heap.pop()
        return o


class MclHeap:

    def __init__(self, array=[]):
        self.heap = array
        n = (len(self.heap) // 2) - 1
        for i in range(n, -1, -1): self.heapify(i)

    def pop(self):
        o = self.heap[0]
        j = len(self.heap)-1
        self.heap[0], self.heap[j] = self.heap[j], self.heap[0]
        del self.heap[j]
        self.heapify(0)
        return o

    def insert(self, v):
        def f(i):
            p = (i - 1) // 2
            if p >= 0:
                if self.heap[i] > self.heap[p]:
                    self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                    f(p)
        self.heap.append(v)
        f(len(self.heap)-1)

    def heapify(self, i):
        n = len(self.heap)
        r = (i + 1) * 2
        l = r - 1
        m = i
        if l < n and self.heap[l] > self.heap[m]: m = l
        if r < n and self.heap[r] > self.heap[m]: m = r
        if m != i:
            self.heap[i], self.heap[m] = self.heap[m], self.heap[i]
            self.heapify(m)