# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 10:15:59 2014

@author: john
"""
class Solution:              
    # @return a list of integers
    def grayCode(self, n):
        result=[]
        for i in range(0,pow(2,n)):
            result.append((i>>1)^i)
        return result
        
if __name__=="__main__":
    solution=Solution()
    print solution.grayCode(3)