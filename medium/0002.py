from common.ListNode import ListNode

""" Add Two Numbers """
# O(n)
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(-1)
        prev = dummy
        while l1 or l2:
            t = carry
            carry = 0
            if l1:
                t += l1.val
                l1 = l1.next
            if l2:
                t += l2.val
                l2 = l2.next
            if t >= 10:
                t = t - 10
                carry = 1
            prev.next = ListNode(t)
            prev = prev.next
        if carry > 0:
            prev.next = ListNode(1)
        return dummy.next