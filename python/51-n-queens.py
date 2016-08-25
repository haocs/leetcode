# source: https://leetcode.com/problems/n-queens/

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def deep_copy(board):
            copy = []
            for row in board:
                # return type are diff as OJ accepted.
                copy.append(''.join(row))
            return copy
            
        def isValidMove(board, n, x, y):
            for i in range(n):
                if board[x][i] == 'Q' or board[i][y] == 'Q':
                    return False
                if (x + i < n and y + i < n and board[x+i][y+i] == 'Q') or \
                    (x + i < n and y - i >= 0 and board[x+i][y-i] == 'Q') or \
                    (x - i >= 0 and y + i < n and board[x-i][y+i] == 'Q') or \
                    (x - i >= 0 and y - i >= 0 and board[x-i][y-i] == 'Q'):
                        return False
            return True
        
        def solve(board, n, row):
            if row == n:
                solutions.append(deep_copy(board))
            else:
                for i in range(n):
                    if board[row][i] == '.' and isValidMove(board, n, row, i):
                        board[row][i] = 'Q'
                        solve(board, n, row + 1)
                    board[row][i] = '.'
        
        solutions = []
        solve([['.'] * n for _ in range(n)], n, 0)
        return solutions
