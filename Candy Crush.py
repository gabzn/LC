https://leetcode.com/problems/candy-crush/

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        def is_valid_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS
        
        def are_cells_equal(x1, y1, x2, y2, x3, y3):
            if is_valid_cell(x1, y1) and is_valid_cell(x3, y3):
                return board[x1][y1] == board[x2][y2] == board[x3][y3]
    
        def find():
            to_crush = set()
            
            for x in range(ROWS):
                for y in range(COLS):
                    if board[x][y] == 0:
                        continue
                    
                    left, right = x - 1, x + 1
                    if are_cells_equal(left, y, x, y, right, y):
                        to_crush.add((left, y))
                        to_crush.add((x, y))
                        to_crush.add((right, y))
                    
                    top, bottom = y - 1, y + 1
                    if are_cells_equal(x, top, x, y, x, bottom):
                        to_crush.add((x, top))
                        to_crush.add((x, y))
                        to_crush.add((x, bottom))
                        
            return to_crush
        
        def crush(to_crush):
            for x, y in to_crush:
                board[x][y] = 0
        
        def drop():
            for y in range(COLS):
                lowest_zero = -1
                
                for x in range(ROWS - 1, -1, -1):
                    if board[x][y] == 0:
                        lowest_zero = max(lowest_zero, x)
                    
                    if board[x][y] != 0 and lowest_zero != -1:
                        board[lowest_zero][y], board[x][y] = board[x][y], board[lowest_zero][y]
                        lowest_zero -= 1
            
        ROWS, COLS = len(board), len(board[0])
        
        while True:
            to_crush = find()
            if not to_crush:
                return board
            
            crush(to_crush)
            drop()
