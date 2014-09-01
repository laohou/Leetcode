class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

            
class Solution:
    
    def deleteDuplicates(self, head):
        if head == None or head.next==None:
            return head
        prev = head
        tmp = prev.next
        while tmp:
            if prev.val != tmp.val:
                prev = tmp
                tmp=tmp.next
            else:
                tmp = tmp.next
                prev.next=tmp
                 
        return head
    
    def printList(self, nodeList):
        while nodeList:
             print '%s--' % (nodeList.val,),
             nodeList = nodeList.next
                
if __name__=="__main__":
    solution = Solution()
    head = ListNode(1)
    one = ListNode(1)
    two=ListNode(2)
    three=ListNode(4)
    four=ListNode(4)
    head.next = one
    one.next=two
    two.next = three
    three.next=four
    solution.printList(solution.deleteDuplicates(head))
