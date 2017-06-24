# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 16:12:24 2014

@author: john
"""
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result=[]
        if numRows==0:
            return result
        result.append([1])
        if numRows==1:
            return result
        result.append([1,1])
        for i in range(2,numRows):
            row=[1]
            for j in range(0,len(result[i-1])-1):
                row.append(result[i-1][j]+result[i-1][j+1])
            row.append(1)
            result.append(row)
        return result
            


if __name__=="__main__":
    solution=Solution()
    print solution.generate(0)