# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""

Implement an iterator over a binary search tree (BST).

Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory,

where h is the height of the tree.
"""

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.push_all(root)


    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0:
            return False
        return True

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.push_all(node.right)
        return node.val

    def push_all(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
if __name__ == '__main__':
    BSTIterator()