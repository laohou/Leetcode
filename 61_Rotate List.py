# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""


from ListUtility import test_list
from ListUtility import print_list
from ListUtility import ListNode

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head:
            return head

        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head
        cur = head

        shift = length - k % length
        while shift:
            cur = cur.next
            shift -= 1

        result = cur.next
        cur.next = None
        return result

if __name__ == '__main__':
    # l = Solution().rotateRight(test_list, 2)
    # print_list(l)



    # l = Solution().rotateRight(test_list, 3)
    # print_list(l)

    node1 = ListNode(1)
    l = Solution().rotateRight(node1, 0)
    print_list(l)
    #
    print ''
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    l = Solution().rotateRight(node1, 2)
    print_list(l)
    #
    print ''
    l = Solution().rotateRight(test_list, 6)
    print_list(l)
