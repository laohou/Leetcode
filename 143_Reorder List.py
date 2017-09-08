# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a singly linked list L: L0?L1?…?Ln-1?Ln,
reorder it to: L0?Ln?L1?Ln-1?L2?Ln-2?…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        cur = head
        while cur.next and stack and cur != stack[-1] and cur.next != stack[-1]:
            node = stack.pop()
            temp = cur.next
            cur.next = node
            node.next = temp
            cur = temp
        if cur == stack[-1]:
            cur.next = None
        elif cur.next == stack[-1]:
            cur.next.next = None


from ListUtility import print_list,test_list
if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    #node3.next = node4
    Solution().reorderList(node1)
    print_list(node1)
    print
    Solution().reorderList(test_list)
    print_list(test_list)

    print
    node5 = ListNode(5)
    Solution().reorderList(node5)
    print_list(node5)

    print
    node6 = ListNode(6)
    node7 = ListNode(7)
    node6.next = node7
    Solution().reorderList(node6)
    print_list(node6)