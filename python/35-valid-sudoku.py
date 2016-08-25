# source: https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def valid_row(board):
            counter = set()
            for row in board:
                for i in row:
                    if i in counter:
                        return False
                    if i != '.':
                        counter.add(i)
                counter.clear()
            return True
                    
        def valid_col(board):
            counter = set()
            for j in range(9):
                for i in range(9):
                    if board[i][j] in counter:
                        return False
                    if board[i][j] != '.':
                        counter.add(board[i][j])
                counter.clear()
            return True
            
        def valid_box(board):
            counter = set()
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    for row in range(3):
                        for col in range(3):
                            num = board[i+row][j+col]
                            if num in counter:
                                return False
                            if num != '.':
                                counter.add(num)
                    counter.clear()
            return True
                    
        
        return valid_row(board) and valid_col(board) and valid_box(board)
