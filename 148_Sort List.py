# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Sort a linked list in O(n log n) time using constant space complexity.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        fast = slow
        slow = slow.next
        fast.next = None
        head1 = self.sortList(head)
        head2 = self.sortList(slow)
        return self.merget_list(head1, head2)

    def merget_list(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        result = None
        if head1.val < head2.val:
            result = head1
            head1 = head1.next
        else:
            result = head2
            head2 = head2.next
        cur = result
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next

        while head1:
            cur.next = head1
            head1 = head1.next
            cur = cur.next
        while head2:
            cur.next = head2
            head2 = head2.next
            cur = cur.next

        return result

import ListUtility
if __name__ == '__main__':
    node1 = ListNode(4)
    node2 = ListNode(7)
    node3 = ListNode(2)
    node4 = ListNode(1)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    head1 = Solution().sortList(node1)
    ListUtility.print_list(head1)