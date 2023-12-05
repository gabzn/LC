https://leetcode.com/problems/battleships-in-a-board/

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROWS, COLS = len(board), len(board[0])
        HORIZONTAL_DIRECTIONS = [(-1, 0), (1, 0)]
        VERTICAL_DIRECTIONS = [(0, -1), (0, 1)]
        
        def is_valid_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS and board[x][y] == 'X'
        
        def check_horizontally(r, c):
            stack = [(r, c)]
            
            while stack:
                x, y = stack.pop()
                visited.add((x, y))
                
                for offset_x, offset_y in HORIZONTAL_DIRECTIONS:
                    adjacent_x, adjacent_y = offset_x + x, offset_y + y
                    
                    if is_valid_cell(adjacent_x, adjacent_y) and (adjacent_x, adjacent_y) not in visited:
                        stack.append((adjacent_x, adjacent_y))
                
        def check_vertically(r, c):
            stack = [(r, c)]
            
            while stack:
                x, y = stack.pop()
                visited.add((x, y))
                
                for offset_x, offset_y in VERTICAL_DIRECTIONS:
                    adjacent_x, adjacent_y = offset_x + x, offset_y + y
                    
                    if is_valid_cell(adjacent_x, adjacent_y) and (adjacent_x, adjacent_y) not in visited:
                        stack.append((adjacent_x, adjacent_y))
        
        res = 0
        visited = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'X' and (r, c) not in visited:
                    res += 1
                    check_horizontally(r, c)
                    check_vertically(r, c)
        
        return res
