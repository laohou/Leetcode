# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [([root.val], root.val, root)]
        result = []
        while stack:
            arr, arr_sum, node = stack.pop()
            if arr_sum == sum and node.left is None and node.right is None:
                result.append(arr)

            if node.left and arr_sum + node.left.val <= sum:
                temp = arr[:]
                temp.append(node.left.val)
                stack.append((temp, arr_sum + node.left.val, node.left))

            if node.right and arr_sum + node.right.val <= sum:
                arr.append(node.right.val)
                stack.append((arr, arr_sum + node.right.val, node.right))

        return result

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(5)
    node4 = TreeNode(4)

    node2.left = node3
    node2.right = node1
    node1.right = node4


    print Solution().pathSum(node2, 7)