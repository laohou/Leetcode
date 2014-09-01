# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 19:38:28 2014

@author: john
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        preNode=head
        nextNode=None
        tmpNode=None
        preTmpNode=None
        
        if preNode:
            nextNode=preNode.next
            if nextNode:
                head=nextNode
                tmpNode=nextNode.next
        while preNode:
            if nextNode:
                nextNode.next=preNode
                preNode.next=tmpNode
                if preTmpNode:
                    preTmpNode.next=nextNode
            preTmpNode=preNode
            preNode=tmpNode
            if tmpNode:
                nextNode=tmpNode.next
            if nextNode:
                tmpNode=nextNode.next
            else:
                tmpNode=None
        return head
        
    def printList(self,head):
        while head:
            print head.val
            head=head.next
        
if __name__=="__main__":
    head=ListNode(0)
    node1=ListNode(1)
    node2=ListNode(2)
    node3=ListNode(3)
    node4=ListNode(4)
    node5=ListNode(5)
    head.next=node1
#    node1.next=node2
   # node4.next=node5
    solution=Solution()
    solution.printList(solution.swapPairs(head))
        
        