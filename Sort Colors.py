# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 14:34:54 2014

@author: john
"""

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def swap(self,A,a,b):
        tmp=A[a]
        A[a]=A[b]
        A[b]=tmp       
            
    
    def sortColors(self, A):
        if A==None:
            return
        red=0
        length=len(A)
        for i in range(0,length):
            if A[i]==0:
                self.swap(A,red,i)
                red=red+1
        white=red
        for i in range(red,length):
            if A[i]==1:
                self.swap(A,white,i)
                white=white+1
#get it wrong,colors in same color...
#I should be more careful next time!!!
#I misunderstood the problem...!
    def sortColorsFails1(self,A):
        length=len(A)
        if length<2:
            return 
        reds=0
        whites=0
        blues=0     
        for i in range(0,length):
            if A[i]==0:
                reds=reds+1
            elif A[i]==1:
                whites=whites+1
            else:
                blues=blues+1
        i=0       
        while i<length:
            if reds:
                A[i]=0
                i=i+1
                reds=reds-1
            if whites and i<length:
                A[i]=1
                i=i+1
                whites=whites-1
            if blues and i<length:
                A[i]=2
                i=i+1
                blues=blues-1
                
if __name__=="__main__":
    solution=Solution()
    A=[1,2,1]
    solution.sortColorsFails1(A)
    print A