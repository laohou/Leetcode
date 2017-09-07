# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.min_dep = sys.maxint

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.getDepthRecur(root, 1)
        return self.min_dep

    def getDepthRecur(self, root, height):
        if height >= self.min_dep:
            return
        if root:
            if root.left is None and root.right is None:
                if height < self.min_dep:
                    self.min_dep = height
            else:
                if root.left:
                    self.getDepthRecur(root.left, height+1)
                if root.left:
                    self.getDepthRecur(root.right, height+1)



if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    root.right = node2
    print Solution().minDepth(root)