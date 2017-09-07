# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return None

        dummy = TreeLinkNode(-1)
        node = dummy
        while root:
            while root:
                node.next = root.left
                node = node.next or node
                node.next = root.right
                node = node.next or node
                root = root.next
            root, node = dummy.next, dummy


if __name__ == '__main__':
    node1 = TreeLinkNode(1)
    node2 = TreeLinkNode(2)
    node3 = TreeLinkNode(3)
    node4 = TreeLinkNode(4)
    node5 = TreeLinkNode(5)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    Solution().connect(node1)
