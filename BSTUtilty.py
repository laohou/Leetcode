# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def build_inorder_bst_tree(nums):
    root = None
    for num in sorted(nums):
        root = TreeNode()

    return root


def print_bst_tree_inorder(root):
    if root:
        print root.val
    if root.left:
        print_bst_tree_inorder(root.left)
    if root.right:
        print_bst_tree_inorder(root.right)

#TODO: print a tree in depth
def print_bst_tree_in_depth(root):
    stack = []
    depth = 0
    if root:
        print '[%d]' % root.val


    pass
if __name__ == '__main__':
    pass