""" Remove Duplicates from Sorted List II """
from utils.ListNode import ListNode


class Solution(object):
    def deleteDuplicates(self, head):
        prev = root = ListNode(None, head)
        prev2 = None
        node = head
        x = 0
        while node:
            if prev.val == node.val: x += 1
            else:
                if x > 0:
                    prev2.next = node
                    x = 0
                else: prev2 = prev
                prev = node
            node = node.next
        if x > 0: prev2.next = node
        return root.next