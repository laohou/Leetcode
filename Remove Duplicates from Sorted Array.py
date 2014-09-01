# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 21:05:18 2014

@author: john
"""

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
       if len(A)<1:
           return len(A)
       back=0
       forth=1
       while forth < len(A):
           if A[back]!=A[forth]:
              back=back+1
              A[back]=A[forth]
           forth=forth+1
       return back+1
        
    def removeDuplicates2(self, A):
        i=0
        length=len(A)
        while i < length-1:
            if A[i+1]==A[i]:
                A[i]
                length=length-1
                i=i-1     
            i = i + 1
        return length
        
        

if __name__=="__main__":
    solution=Solution()
    print solution.removeDuplicates([1,1,2,2,3,3,4,4,5,6,7,8,9,9])