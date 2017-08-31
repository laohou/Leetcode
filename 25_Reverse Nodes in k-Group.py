__author__ = 'yghou'
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverse(self, head, end):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = head.next
        cur = prev.next
        while cur != end:
            prev.next = cur.next
            cur.next = head.next
            head.next = cur
            cur = prev.next

        return prev

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or k == 1:
            return head


        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        i = 0
        while head:
            i += 1
            if i % k == 0:
                prev = self.reverse(prev, head.next)
                head = prev.next
            else:
                head = head.next


        return dummy.next


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

    #res = s.reverse(node1, node4)
    res = s.reverseKGroup(node1, 2)
    from ListUtility import print_list
    print_list(res)