# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = 'yghou'


"""
Reverse a linked list from position m to n.
Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        prem = dummy
        for x in range(1, m):
            prem = prem.next

        prev, cur = None, prem.next
        while cur and m <= n:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            m += 1


        prem.next.next = cur
        prem.next = prev

        return dummy.next



def print_list(node):
    tmp = node
    while tmp:
        print('%d-->'%(tmp.val), end='')
        tmp = tmp.next


if __name__ == '__main__':
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    rel = s.reverseBetween(node1, 3, 5)
    print_list(rel)

