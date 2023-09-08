https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def is_valid_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS and (x, y) not in visited_cells
        
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        queue = deque()
        visited_cells = set()
        
        # Get all the cells in the edges
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                    queue.append((r, c))
                    visited_cells.add((r, c))
                    
        while queue:
            x, y = queue.popleft()
            if board[x][y] == 'X':
                continue
            
            # The current cell is O, we change it to E and perform BFS on this cell
            # to find all the adjacent O's
            board[x][y] = 'E'
            for offset_x, offset_y in DIRECTIONS:
                adjacent_x, adjacent_y = x + offset_x, y + offset_y
                
                if is_valid_cell(adjacent_x, adjacent_y):
                    visited_cells.add((adjacent_x, adjacent_y))
                    queue.append((adjacent_x, adjacent_y))
        
        # If there's any O remaining in the board, they can be captured
        # Change all the E back to O, these O's cannot be captured
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'E':
                    board[r][c] = 'O'
