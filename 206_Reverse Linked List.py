__author__ = 'yghou'
"""
Reverse a singly linked list.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        head = prev
        return head