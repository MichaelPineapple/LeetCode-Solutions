""" Partition List """
from utils.ListNode import ListNode


class Solution(object):
    def partition(self, head, x):
        dummy = ListNode(None, head)
        node = head
        less, greater = [], []
        while node:
            if node.val < x: less.append(node)
            else: greater.append(node)
            nxt = node.next
            node.next = None
            node = nxt
        less.extend(greater)
        node = dummy
        for n in less:
            node.next = n
            node = node.next
        return dummy.next