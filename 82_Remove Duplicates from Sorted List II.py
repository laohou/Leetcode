# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a sorted linked list, delete all nodes that have duplicate numbers,

leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.


"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy
        is_duplicate = False
        while cur and cur.next:
            #其实这个while循环比较关键，实际应用中应该小心，防止造成内存泄漏
            while cur.next.next and cur.next.val == cur.next.next.val:
                cur.next = cur.next.next
                is_duplicate = True

            if is_duplicate:
                cur.next = cur.next.next
                is_duplicate = False
            else:
                cur = cur.next

        return dummy.next


if __name__ == '__main__':

    from ListUtility import build_list, print_list


    l1 = build_list([1, 2, 3, 3, 4, 4, 5])
    l2 = build_list([1, 1, 1, 2, 3])

    l3 = build_list([1, 1])
    l4 = build_list([1, 2, 2])

    print_list(Solution().deleteDuplicates(l1))
    print
    print_list(Solution().deleteDuplicates(l2))
    print
    print_list(Solution().deleteDuplicates(l3))
    print
    print_list(Solution().deleteDuplicates(l4))


if __name__ == '__main__':
    Solution()