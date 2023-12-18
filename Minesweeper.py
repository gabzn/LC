https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def is_a_valid_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS
        
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), 
                      (-1, -1), (1, 1), (-1, 1), (1, -1)]
        
        click_x, click_y = click
        
        if board[click_x][click_y] == 'M':
            board[click_x][click_y] = 'X'
            return board
        
        visited_cells = set([(click_x, click_y)])
        queue = deque([(click_x, click_y)])
        
        while queue:
            x, y = queue.popleft()

            mines = 0
            adjacent_cells = []
            
            # Look at all 8 surrounding cells
            for offset_x, offset_y in DIRECTIONS:
                adjacent_x, adjacent_y = x + offset_x, y + offset_y
                
                # If this is not a valid cell or this cell has been visited, go to the next one
                if not is_a_valid_cell(adjacent_x, adjacent_y) or (adjacent_x, adjacent_y) in visited_cells:
                    continue
                
                # If the neighbouring cell is a mine, increment the count and don't let the mine into the queue
                if board[adjacent_x][adjacent_y] == 'M':
                    mines += 1
                else:
                    adjacent_cells.append((adjacent_x, adjacent_y))
                    # visited_cells.add((adjacent_x, adjacent_y))   no good
            
            # If there's no mines, change current cell to B and push all surrounding cells to queue
            if mines == 0:
                board[x][y] = 'B'

                for adjacent_cell in adjacent_cells:
                    queue.append(adjacent_cell)
                    visited_cells.add(adjacent_cell)
            else:
                board[x][y] = str(mines)
        
        return board
