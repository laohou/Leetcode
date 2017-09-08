# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        fast, slow = head.next.next, head
        steps1 = 1
        steps2 = 1
        while fast and fast.next and fast != slow:
            slow = slow.next
            fast = fast.next.next
            steps1 += 1
            steps2 += 1

        if not fast or not fast.next:
            return None
        steps2 += 1
        fast = fast.next.next
        slow = slow.next
        while fast and fast.next and fast != slow:
            slow = slow.next
            fast = fast.next.next
            steps2 += 1

        cycle_len = steps2 - steps1

        start, end = head, head
        for i in range(cycle_len):
            end = end.next
        while start != end:
            start = start.next
            end = end.next

        return start


if __name__ == '__main__':
    # node1 = ListNode(1)
    # node2 = ListNode(2)
    # node1.next = node2
    # node2.next = node1
    # Solution().detectCycle(node1)

    node1 = ListNode(1)
    node1.next = node1
    Solution().detectCycle(node1)