from utils.RndNode import RndNode

""" Copy List With Random Pointer """
# O(n)
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        nodeMap, nodeList, node, prev, i = {}, [], head, RndNode(0), 0
        while node:
            nodeMap[node], node2 = i, RndNode(node.val)
            prev.next = node2
            nodeList.append(node2)
            node, prev, i = node.next, node2, i+1
        head2 = nodeList[0]
        node, node2 = head, head2
        while node:
            rnd = node.random
            if rnd:
                node2.random = nodeList[nodeMap[rnd]]
            node, node2 = node.next, node2.next
        return head2