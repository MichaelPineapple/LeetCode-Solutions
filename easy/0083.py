class Solution(object):
    def deleteDuplicates(self, head):
        if head is not None:
            n = head
            pv = head.val-1
            pn = None
            while n is not None:
                v = n.val
                if v == pv:
                    pn.next = n.next
                else:
                    pv = v
                    pn = n
                n = n.next
        return head