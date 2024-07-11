from common.ListNode import ListNode

""" Merge Two Sorted Lists """
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        node = head
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        if list2:
            node.next = list2
        else:
            node.next = list1
        return head.next