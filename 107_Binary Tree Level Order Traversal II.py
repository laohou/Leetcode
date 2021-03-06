# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = [[]]
        self._levelOrderBottom(root, 0, result)
        return result[::-1]

    def _levelOrderBottom(self, root, level, result):
        if root:
            if len(result) < level+1:
                result.append([])
            result[level].append(root.val)
            self._levelOrderBottom(root.left, level+1, result)
            self._levelOrderBottom(root.right, level+1, result)



if __name__ == '__main__':
    Solution()