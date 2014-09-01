class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        elif l2==None:
            return l1
        prev1 = l1
        prev2 = l2
        l1=l1.next
        l2=l2.next
        l=l1
        if prev1.val < prev2.val:
            l=prev1
            prev1=l1
        else:
            l=prev2
            prev2=l2
        head=l

        while prev1 and prev2:
            if prev1.val < prev2.val:
                l.next=prev1
                prev1=l1
                if l1:
                    l1=l1.next
            else:
                l.next = prev2
                prev2=l2
                if l2:
                    l2=l2.next
            l=l.next

        if prev1:
            l.next = prev1
        elif prev2:
            l.next = prev2
        return head
    
    def printList(self,l):
        while l:
            print(l.val)
            l=l.next
            
if __name__=="__main__":
    solution = Solution()
    a1 = ListNode(1)
    a2 = ListNode(3)
    a3 = ListNode(5)
    a1.next =a2
    a2.next=a3
    b1 = ListNode(2)
    b2=ListNode(4)
    b3=ListNode(6)
    b1.next=b2
    b2.next=b3

    solution.printList(solution.mergeTwoLists(a1,b1))
