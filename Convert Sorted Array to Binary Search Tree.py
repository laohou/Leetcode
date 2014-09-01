# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 16:45:19 2014

@author: john
"""
#Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#Convert Sorted Array to Binary Search Tree 

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def sortedArrayToBSTRecur(self,num,low,high):
        if low == high:
            return TreeNode(num[low])
        elif low > high:
            return None
        middle=(low+high)/2
        root=TreeNode(num[middle])
        root.right=self.sortedArrayToBSTRecur(num,middle+1,high)
        root.left = self.sortedArrayToBSTRecur(num,low,middle-1)
        return root
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        high=len(num)-1
        low=0
        return self.sortedArrayToBSTRecur(num,low,high)
    
    def printTree(self,root):
        if root==None:
            return 
        
        self.printTree(root.left)
        print root.val
        self.printTree(root.right)

if __name__=="__main__":
    solution=Solution()
    solution.printTree(solution.sortedArrayToBST([1,2,3,4,5,6,7,8]))

            