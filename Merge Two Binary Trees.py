# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        newTree = t1 if t1 else t2
        if t1 and t2:
            newTree.val = t1.val + t2.val
            newTree.left = self.mergeTrees(t1.left, t2.left)
            newTree.right = self.mergeTrees(t1.right, t2.right)

        return newTree


    def printTrees(self, t):
        if t:
            print t.val
            self.printTrees(t.left)
            self.printTrees(t.right)


if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t11 = TreeNode(3)
    t12 = TreeNode(2)
    t13 = TreeNode(5)
    t1.left = t11
    t1.right = t12
    t11.left = t13

    t2 = TreeNode(2)
    t21 = TreeNode(1)
    t22 = TreeNode(3)
    t23 = TreeNode(4)
    t24 = TreeNode(7)
    t2.left = t21
    t2.right = t22
    t21.right = t23
    t22.right = t24

    s.printTrees(t1)
    print '----'
    s.printTrees(t2)

    print '--result---------'
    nt = s.mergeTrees(t1, t2)
    s.printTrees(nt)



