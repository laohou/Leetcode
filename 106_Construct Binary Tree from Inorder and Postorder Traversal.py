# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given inorder and postorder traversal of a tree, construct the binary tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if len(postorder) == 0 or len(inorder) == 0 or len(postorder) != len(inorder):
            return None

        inorder_map = {}
        for pos, val in enumerate(inorder):
            inorder_map[val] = pos


        root = TreeNode(postorder[-1])
        for i in range(len(postorder)-2, -1, -1):
            curr = root
            while True:
                if inorder_map[postorder[i]] > inorder_map[curr.val]:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = TreeNode(postorder[i])
                        break
                else:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = TreeNode(postorder[i])
                        break

        return root


if __name__ == '__main__':
    Solution()