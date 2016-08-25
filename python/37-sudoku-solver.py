# source: https://leetcode.com/problems/sudoku-solver/

class Solution(object):
    def isValidMove(self, board, x, y, val): # -> bool
        for i in range(9):
            if board[i][y] == val or board[x][i] == val:
                return False
        x0 = x // 3 * 3
        y0 = y // 3 * 3
        for i in range(3):
            for j in range(3):
                if board[x0+i][y0+j] == val:
                    return False
                    
        return True
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def _x(idx):
            return int(idx/9)
            
        def _y(idx):
            return int(idx%9)
            
        def move(board, idx): # -> bool
            if idx == 81:
                return True
            x = _x(idx)
            y = _y(idx)
            if board[x][y] == '.':
                for num in range(1, 10):
                    val = str(num)
                    if self.isValidMove(board, x, y, val):
                        board[x][y] = val
                        if move(board, idx + 1):
                            return True
                board[x][y] = '.'
                return False
            
            return move(board, idx+1)
        
        move(board, 0)
