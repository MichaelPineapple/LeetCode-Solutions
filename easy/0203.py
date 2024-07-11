class Solution(object):
    def removeElements(self, head, val):
        n, p = head, None
        while n is not None:
            nxt = n.next
            if val == n.val:
                if p is None:
                    head = nxt
                else:
                    p.next = nxt
            else:
                p = n
            n = nxt
        return head