# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a linked list and a value x,

partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,

Given 1->4->3->2->5->2 and x = 3,

return 1->2->2->4->3->5.

"""

from ListUtility import ListNode, print_list, build_list

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        cur = head
        higher_head = lower_head = None
        high_cur = lower_cur = None

        while cur:
            if cur.val >= x:
                if not higher_head:
                    high_cur =higher_head = cur
                else:
                    high_cur.next = cur
                    high_cur = high_cur.next
            else:
                if not lower_head:
                    lower_cur = lower_head = cur
                else:
                    lower_cur.next = cur
                    lower_cur = cur
            cur = cur.next
        if high_cur:
            high_cur.next = None
        if lower_cur:
            lower_cur.next = higher_head

        return lower_head if lower_head else higher_head

if __name__ == '__main__':
    # l1 = build_list([1, 4, 3, 2, 5, 2])
    # l = Solution().partition(l1, 3)
    # print
    # print_list(l)

    # l2 = build_list([3, 4, 3, 1, 5, 2])
    # l = Solution().partition(l2, 2)
    # print
    # print_list(l)

    l3 = build_list([1,1])
    l = Solution().partition(l3, 0)
    print
    print_list(l)