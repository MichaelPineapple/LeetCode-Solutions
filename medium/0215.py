from utils import MaxHeap

""" Kth Largest Element In An Array """
# O(n*log[n]) <-- just as good as sorting SMH ToDo
class Solution(object):
    def findKthLargest(self, nums, k):
        MaxHeap.build(nums)
        o = None
        for _ in range(k): o = MaxHeap.pop(nums)
        return o