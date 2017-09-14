# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        dummy1 = headA
        dummy2 = headB
        a_len = 1
        b_len = 1
        while dummy1.next:
            dummy1 = dummy1.next
            a_len += 1
        while dummy2.next:
            dummy2 = dummy2.next
            b_len += 1
        if dummy1 != dummy2:
            return None

        dummy1 = headA
        dummy2 = headB

        if a_len > b_len:
            tmp = a_len - b_len
            while tmp > 0:
                dummy1 = dummy1.next
                tmp -= 1
        elif a_len < b_len:
            tmp = b_len - a_len
            while tmp > 0:
                dummy2 = dummy2.next
                tmp -= 1
        while dummy1 and dummy2 and dummy1 != dummy2:
            dummy1 = dummy1.next
            dummy2 = dummy2.next

        return dummy1
if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(1)
    node4 = ListNode(1)
    c_node = ListNode(100)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = c_node

    node5 = ListNode(2)
    node6 = ListNode(101)
    node5.next = c_node
    c_node.next = node6

    from ListUtility import print_list
    print_list(Solution().getIntersectionNode(node1,node5))