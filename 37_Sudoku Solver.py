__author__ = 'yghou'
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for row in range(9):
            board[row] = list(board[row])

        self.recursive(board, 0, 0)

        for row in range(9):
            board[row] = "".join(board[row])

        pass

    def recursive(self, board, i, j):
        if j >= 9:
            return self.recursive(board, i+1, 0)
        if i == 9:
            return True

        if board[i][j] == '.':
            for num in range(1, 10):
                s_num = str(num)
                if all(s_num != board[i][col] for col in range(9)) \
                    and all(s_num != board[row][j] for row in range(9))\
                    and all(s_num != board[i//3*3 + count//3][j//3*3 + count % 3] for count in range(9)):
                    board[i][j] = s_num

                    if not self.recursive(board, i, j+1):
                        board[i][j] = '.'
                    else:
                        return True
        else:
            return self.recursive(board, i, j+1)

        return False

if __name__ == '__main__':
    sudoku = ["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6",
              "...2759.."]
    Solution().solveSudoku(sudoku)
    assert sudoku == ['519748632', '783652419', '426139875', '357986241', '264317598', '198524367', '975863124',
                      '832491756', '641275983']