# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Sort a linked list using insertion sort.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from ListUtility import print_list

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        sorted_list = ListNode(-1)
        cur = head
        while cur:
            nxt = cur.next
            prev = sorted_list
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
            cur.next = prev.next
            prev.next = cur
            cur = nxt

        return sorted_list.next



if __name__ == '__main__':
    node1 = ListNode(2)
    node2 = ListNode(1)
    node1.next = node2
    print_list(Solution().insertionSortList(node1))