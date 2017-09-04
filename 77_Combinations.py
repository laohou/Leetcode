# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given two integers n and k,

return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution(object):

    def combinations(self, iterable, r):
        # combinations('ABCD', 2) --> AB AC AD BC BD CD
        # combinations(range(4), 3) --> 012 013 023 123
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = range(r)
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
            yield tuple(pool[i] for i in indices)

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        for i in self.combinations(range(1, n+1), k):
            result.append(list(i))
        return result

    def combineRecr(self, n, k):

        if k == 1:
            return [[i+1] for i in range(n)]

        result = []

        if n > k:
            result = [r + [n] for r in self.combineRecr(n-1, k-1)] + self.combineRecr(n-1, k)
        else:
            result = [r + [n] for r in self.combineRecr(n-1, k-1)]

        return result

if __name__ == '__main__':
    print Solution().combine(4, 2)
    print Solution().combineRecr(4, 2)