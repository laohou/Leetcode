# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 13:28:26 2014

@author: john
"""
#reversely merge two arrays put them in the tail
# and move the merged array to the front of array A
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        last=len(A)-1
        a=m-1
        b=n-1
        while a>=0 and b>=0:
            if A[a]>B[b]:
                A[last]=A[a]
                a=a-1
            else:
                A[last]=B[b]
                b=b-1
            last=last-1

        while a>=0:
            A[last]=A[a]
            last=last-1
            a=a-1
        while b>=0:
            A[last]=B[b]
            last=last-1
            b=b-1
        last=last+1
        for i in range(0,m+n):
            A[i]=A[last]
            last=last+1
            
if __name__=="__main__":
    solution=Solution()
    A=[2,3,5,7,9,12,15,0,0,0,0,0]#7,12
    B=[1,4,8,50,70,]#5
    solution.merge(A,7,B,5)
    print A
