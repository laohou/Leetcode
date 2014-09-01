# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 17:33:59 2014

@author: john
"""
class Solution:

    def generate(self,n,svv):
        try:
            return svv[n]
        except:
            sv=[]
            for i in range(0,n)[::-1]:
                left=self.generate(i,svv)
                right=self.generate(n-1-i,svv)
                for j in range(0,len(left)):
                    for k in range(0,len(right)):
                        string=""
                        string+="("
                        #str([])='[]'
                        if str(left[j])!='[]':
                            string+=str(left[j])
                        string+=")"
                        if str(right[k])!='[]':
                            string+=str(right[k])
                        sv.append(string) 
            svv.append(sv)
            return sv
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        #first item is just for python
        svv=[[[]],["()"]]
        if n==0:
            return ""
        return self.generate(n,svv)
        
if __name__=="__main__":
    solution=Solution()
    print solution.generateParenthesis(2)