# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a singly linked list where elements are sorted in ascending order,

convert it to a height balanced BST.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.cur = None

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        length = 0
        node = head
        while node:
            node = node.next
            length += 1

        self.cur = head
        return self.build_tree(0, length-1)

    def build_tree(self, start, end):
        if start > end:
            return None
        mid = (end+start) // 2
        left = self.build_tree(start, mid-1)
        root = TreeNode(self.cur.val)
        root.left = left
        self.cur = self.cur.next
        right = self.build_tree(mid+1, end)
        root.right = right
        return root

if __name__ == '__main__':
    from ListUtility import test_list
    Solution().sortedListToBST(test_list)