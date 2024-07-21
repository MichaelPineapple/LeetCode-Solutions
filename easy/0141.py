""" Linked List Cycle """
class Solution(object):
    def hasCycle(self, head):
        s = set()
        while head is not None:
            if head in s: return True
            s.add(head)
            head = head.next
        return False