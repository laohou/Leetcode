class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self,root):
        if root == None:
            return None
    
        curlvl = root
        prelvl = None
        while curlvl:
            curNode = curlvl
            while curNode:
                if curNode = prelvl.left:
                    curNode.next = prelvl.right
                else:
                    prelvl = prelvl.next
                    curNode.next = prelvl.right
                curNode = curNode.next
     
            prelvl = curlvl
            curlvl = curlvl.left if curlvl.left else curlvl.right
   
