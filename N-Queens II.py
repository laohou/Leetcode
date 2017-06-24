class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.result = 0
        board = [['.'] * n for i in range(n)]
        self.solveNQ(board, n, 0)
        return self.result

    def isSafe(self, board, n, row, col):
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        i = row
        j = col
        while i>=0 and j>=0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i = row
        j = col
        while i<n and j>=0:
            if board[i][j] == 'Q':
                return False
            i += 1
            j -= 1
        return True


    def solveNQ(self, board, n, col):

        if col >= n:
            self.result += 1
            return True

        for i in range(n):
            if self.isSafe(board, n, i, col):

                board[i][col] = 'Q'
                self.solveNQ(board, n, col+1)
                board[i][col] = '.'

        return False

if __name__ == '__main__':
    s = Solution()
    print s.totalNQueens(4)
    print s.totalNQueens(5)