# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward.

Could you devise a constant space solution?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.node1 = None
        self.node2 = None
        self.prev = None

    def _recur(self, root):
        if not root:
            return
        self._recur(root.left)

        if self.prev:
            if root.val < self.prev.val:
                if not self.node1:
                    self.node1 = self.prev
                self.node2 = root

        self.prev = root
        self._recur(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self._recur(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val

if __name__ == '__main__':
    Solution()