# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,

where "adjacent" cells are those horizontally or vertically neighboring.

The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.dfs_exist(board, i, j, m, n, word):
                    return True

        return False

    def dfs_exist(self, board, i, j, m, n, word):
        if len(word) == 0:
            return True

        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[0]:
            return False

        temp = board[i][j]
        board[i][j] = '.'
        target = word[1:]
        result = self.dfs_exist(board, i-1, j, m, n, target)\
                 or self.dfs_exist(board, i+1, j, m, n, target) \
                 or self.dfs_exist(board, i, j-1, m, n, target) \
                 or self.dfs_exist(board, i, j+1, m, n, target)

        board[i][j] = temp
        return result

if __name__ == '__main__':
    m = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    assert Solution().exist(m, 'ABCCED')
    assert Solution().exist(m, 'SEE')
    assert not Solution().exist(m, 'ABCB')