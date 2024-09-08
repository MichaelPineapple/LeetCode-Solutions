""" Merge K Sorted Lists """
from utils.ListNode import ListNode

# O(n^2)
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        node = dummy
        while True:
            minval, mindex = float('inf'), None
            for i, n in enumerate(lists):
                if n is not None:
                    nv = n.val
                    if nv < minval: mindex, minval = i, nv
            if mindex is None: break
            minode = lists[mindex]
            node.next = minode
            node = node.next
            lists[mindex] = minode.next
        return dummy.next