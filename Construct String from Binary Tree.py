# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ans = ''
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        ans = ''
        if t:
            ans += str(t.val)

            left = self.tree2str(t.left)
            right = self.tree2str(t.right)

            if left == '' and right == '':
                return ans
            elif left == '':
                ans += ('()'+'('+right+')')
            elif right == '':
                ans += '('+left+')'
            else:
                ans += '(' + left + ')' + '(' + right + ')'
        else:
            return ''

        return ans

if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t1.left = t2
    t1.right = t3
    t2.right = t4
    t2.left = TreeNode(None)

    print s.tree2str(t1)
