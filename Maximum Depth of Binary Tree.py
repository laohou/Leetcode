# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return 1
        lDepth = maxDepth(root.left)+1
        rDepth = maxDepth(root.right)+1
        return lDepth if lDepth > rDepth else rDepth

if __name__=="__main__":
    root = TreeNode(0)
    solution = Solution()
    print solution.maxDepth(root)
