""" Rotate List """
from utils.ListNode import ListNode


class Solution(object):
    def rotateRight(self, head, k):
        if k == 0: return head
        if not head: return head
        dummy = ListNode(None, head)
        node = head
        stack = []
        while node:
            stack.append(node)
            nxt = node.next
            node.next = None
            node = nxt
        node = dummy
        n = len(stack)
        x = n - (k % n)
        stack[:x] = stack[:x][::-1]
        stack[x:] = stack[x:][::-1]
        while len(stack) > 0:
            p = stack.pop()
            node.next = p
            node = node.next
        return dummy.next
