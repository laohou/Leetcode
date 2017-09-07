# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values.

(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        stack = [[root]]
        level_stack = [[root]]
        while stack:
            parents = stack.pop()
            temp = []
            for parent in parents:
                if parent.left:
                    temp.append(parent.left)
                if parent.right:
                    temp.append(parent.right)
            if len(temp) > 0:
                level_stack.append(temp)
                stack.append(temp)
        result = []
        for i, level in enumerate(level_stack):
            temp = []
            for node in level:
                temp.append(node.val)
            if i % 2 == 1:
                result.append(temp[::-1])
            else:
                result.append(temp)
        return result
if __name__ == '__main__':
    root = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)

    root.left = node9
    root.right = node20
    node20.left = node15
    node20.right = node7


    print Solution().zigzagLevelOrder(root)