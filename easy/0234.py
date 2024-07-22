""" Palindrome Linked List """
# O(n)
class Solution(object):
    def isPalindrome(self, head):
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        stack = []
        e = (n % 2 == 0)
        h = n // 2
        i = 0
        node = head
        while node:
            v = node.val
            if i < h:
                stack.append(v)
            elif (i > h) or (i == h and e):
                if stack.pop() != v: return False
            node = node.next
            i += 1
        return True
# ToDo - Improve space complexity from O(n) to O(1)