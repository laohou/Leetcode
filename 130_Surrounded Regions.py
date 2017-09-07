# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return
        queue = []
        for i in range(m):
            for j in range(n):
                if (i in (0, m-1) or j in (0, n-1)) and board[i][j] == 'O':
                    queue.append((i, j))


        while queue:
            i, j = queue.pop(0)
            board[i][j] = 'M'
            if 0 <= i+1 < m and board[i+1][j] == 'O':
                queue.append((i+1, j))
            if 0 <= i-1 < m and board[i-1][j] == 'O':
                queue.append((i-1, j))
            if 0 <= j+1 < n and board[i][j+1] == 'O':
                queue.append((i, j+1))
            if 0 <= j-1 < n and board[i][j-1] == 'O':
                queue.append((i, j-1))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

if __name__ == '__main__':
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    b2 = [['O']]
    Solution().solve(b2)
    print b2