# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given preorder and inorder traversal of a tree, construct the binary tree.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 or len(inorder) == 0 or len(preorder) != len(inorder):
            return None

        inorder_map = {}
        for pos, val in enumerate(inorder):
            inorder_map[val] = pos

        root = TreeNode(preorder[0])
        for val in preorder[1:]:
            curr = root
            while True:
                if inorder_map[val] < inorder_map[curr.val]:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = TreeNode(val)
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = TreeNode(val)
                        break
        return root


if __name__ == '__main__':
    Solution().buildTree([1, 2], [2, 1])