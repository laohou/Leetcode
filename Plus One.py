# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 16:35:58 2014

@author: john
"""

class Solution:
    
    def plusOne(self,digits):
        if digits == None:
            return None
        hasCarry=False
        length=len(digits)
        if digits[length-1]<9:
            digits[length-1]=digits[length-1]+1
        else:
            digits[length-1]=0
            hasCarry=True
        for i in range(0,len(digits)-1)[::-1]:
            if hasCarry==False:
                return digits
            if digits[i]<9:
                digits[i]=digits[i]+1
                hasCarry=False
            else:
                digits[i]=0
                
        if digits[0]==0:
            result=[1]
            result.extend(digits)
            return result
        return digits
            
    # @param digits, a list of integer digits
    # @return a list of integer digits
# misunderstood the problem again!!
    def plusOneFails(self, digits):
        if digits == None:
            return None
        hasCarry=False
        length=len(digits)
        if digits[length-1]==0:
            digits[length-1]=1
            return digits
        else:
            digits[length-1]=0
            hasCarry=True

        for i in range(0,len(digits)-1)[::-1]:
            if hasCarry==False:
                return digits
            if digits[i]&0x01==0:
                digits[i]=1
                hasCarry=False
            elif digits[i]&0x01==1:
                digits[i]=0
        if digits[0]==1:
            result=[0]
            result.extend(digits)
            return result
        return digits
if __name__=="__main__":
    solution=Solution()
    arr=[2,4,9,9    ,9]
    print solution.plusOne(arr)