# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 14:15:57 2014

@author: john
"""

#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def isSameTree(self,p, q):
        if p==None and q==None:
            return True
        elif p==None or q==None:
            return False
            
        if p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
    def mirror(self,root):
        if root:
            tmpNode = root.right
            root.right = root.left
            root.left = tmpNode
            self.mirror(root.left)
            self.mirror(root.right)
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root==None:
            return True
        self.mirror(root.left)
        return self.isSameTree(root.left,root.right)