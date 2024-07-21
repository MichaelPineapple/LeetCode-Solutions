""" Intersection of Two Linked Lists """
# O(n)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next
        while headB:
            if headB in s: return headB
            headB = headB.next
        return None