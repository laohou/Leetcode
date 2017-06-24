# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 20:25:45 2014

@author: john
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    
    def getHeight(self,root):
        if root==None:
            return 0
        rHeight=self.getHeight(root.right)+1
        lHeight=self.getHeight(root.left)+1
        height= rHeight if rHeight > lHeight else lHeight
        return height
         
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root==None:
            return True
        rH = self.getHeight(root.right)
        rL = self.getHeight(root.left)
        
        if abs(rH - rL)>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__=="__main__":
    solution = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5= TreeNode(5)
    
    node1.left=node2
    node2.left=node4

    print solution.isBalanced(node1)