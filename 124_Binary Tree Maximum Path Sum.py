# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some

starting node to any node in the tree along the parent-child connections.

The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution(object):
    def __init__(self):
        self.max_sum = 0
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = root.val
        self.maxPathSumRecur(root)
        return self.max_sum

    def maxPathSumRecur(self, root):
        if root:
            if not root.left and not root.right:
                if root.val > self.max_sum:
                    self.max_sum = root.val

                return root.val

            left_sum = 0
            right_sum = 0
            if root.left:
                left_sum = self.maxPathSumRecur(root.left)
                left_sum = 0 if left_sum < 0 else left_sum
            if root.right:
                right_sum = self.maxPathSumRecur(root.right)
                right_sum = 0 if right_sum < 0 else right_sum

            self.max_sum = max(self.max_sum, root.val+left_sum+right_sum)
            return max(left_sum, right_sum) + root.val
        else:
            return 0


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    assert Solution().maxPathSum(node1) == 6

    node4 = TreeNode(-3)
    assert Solution().maxPathSum(node4) == -3

    node5 = TreeNode(1)
    node6 = TreeNode(2)
    node5.left = node6
    assert Solution().maxPathSum(node5) == 3

    node7 = TreeNode(1)
    node8 = TreeNode(-2)
    node9 = TreeNode(-3)
    node10 = TreeNode(1)
    node11 = TreeNode(3)
    node12 = TreeNode(-2)
    node13 = TreeNode(-1)

    node7.left = node8
    node7.right = node9
    node8.left = node10
    node8.right = node11
    node10.left = node13
    node9.left = node12

    assert Solution().maxPathSum(node7) == 3

    node13 = TreeNode(-1)
    node14 = TreeNode(-2)
    node13.left = node14
    assert Solution().maxPathSum(node13) == -1