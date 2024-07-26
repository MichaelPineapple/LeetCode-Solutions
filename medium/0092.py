from utils.ListNode import ListNode

""" Reverse Linked List II """
class Solution(object):
    def reverseBetween(self, head, left, right):
        root = ListNode(-1, head)
        node = root
        stack = []
        i = 0

        while i < left - 1:
            node = node.next
            leftTail = node
            i += 1

        leftTail = node
        prev = node
        node = node.next
        i += 1

        while i <= right:
            stack.append(node)
            prev.next = None
            prev = node
            node = node.next
            i += 1

        prev.next = None
        rightHead = node
        node = leftTail

        while len(stack) > 0:
            p = stack.pop()
            node.next = p
            node = node.next

        node.next = rightHead
        return root.next