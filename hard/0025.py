from utils.ListNode import ListNode
""" Reverse Nodes in K-Group """
# O(n)
class Solution(object):
    def reverseKGroup(self, head, k):
        prev = leftTail = root = ListNode(-1, head)
        node = head
        stack = []
        i = 0
        while prev:
            if i == k:
                i = 0
                tmp = stack[0]
                self.reverse(leftTail, node, stack)
                leftTail = tmp
            stack.append(node)
            prev = node
            if node: node = node.next
            i += 1
        return root.next

    def reverse(self, leftTail, rightHead, stack):
        node = leftTail
        while len(stack) > 0:
            p = stack.pop()
            node.next = p
            node = node.next
        node.next = rightHead