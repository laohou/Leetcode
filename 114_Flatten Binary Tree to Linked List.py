# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
If you notice carefully in the flattened tree,

each node's right child points to the next node of a pre-order traversal.

"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        stack = []

        self.pre_order_transvers(root, stack)

        for i in range(len(stack)-1):
            stack[i].left = None
            stack[i].right = stack[i+1]



    def pre_order_transvers(self, root, stack):
        if root:
            stack.append(root)
            if root.left:
                self.pre_order_transvers(root.left, stack)
            if root.right:
                self.pre_order_transvers(root.right, stack)

if __name__ == '__main__':
    Solution()