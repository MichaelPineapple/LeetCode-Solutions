from common.ListNode import ListNode

""" Remove Nth Node From End of List """
# O(n)? Time
# O(1)? Space
class Solution(object):
    def removeNthFromEnd(self, head, n):
        node = head
        count = 0
        while node:
            node = node.next
            count += 1
        node = head
        k = count - n
        dummy = ListNode(0, head)
        prev = dummy
        for i in range(k):
            prev = node
            node = node.next
        prev.next = node.next
        return dummy.next