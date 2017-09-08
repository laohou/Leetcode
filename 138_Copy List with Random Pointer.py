# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
A linked list is given such that each node contains an additional random pointer

which could point to any node in the list or null.

Return a deep copy of the list.
"""


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head

        cur = head
        while cur:
            cur_cp = RandomListNode(cur.label)
            cur_cp.next = cur.next
            cur.next = cur_cp
            cur = cur_cp.next

        cur = head
        head_cp = head.next
        while cur and cur.next:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        while cur and cur.next and cur.next.next:
            temp = cur.next.next
            cur.next.next = cur.next.next.next
            cur.next = temp
            cur = cur.next
        cur.next = None
        return head_cp


if __name__ == '__main__':
    # node1 = RandomListNode(1)
    # node2 = RandomListNode(2)
    # node3 = RandomListNode(3)
    # node1.next = node2
    # node2.next = node3
    # node1.random = node1
    # node2.random = node3
    # node3.random = node1
    # Solution().copyRandomList(node1)

    node4 = RandomListNode(4)
    Solution().copyRandomList(node4)