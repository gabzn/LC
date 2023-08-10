https://leetcode.com/problems/walls-and-gates/

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        def is_valid_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS
        
        ROWS, COLS = len(rooms), len(rooms[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        visited_cells = set()
        queue = deque()
        
        # Find all the gates first
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        
        # Starting from gates, perform BFS to all other cells.
        while queue:
            x, y = queue.popleft()
            
            if (x, y) in visited_cells:
                continue
            visited_cells.add((x, y))

            for offset_x, offset_y in DIRECTIONS:
                adjacent_x, adjacent_y = offset_x + x, offset_y + y
                
                if is_valid_cell(adjacent_x, adjacent_y) and rooms[adjacent_x][adjacent_y] != -1:
                    rooms[adjacent_x][adjacent_y] = min(rooms[adjacent_x][adjacent_y], rooms[x][y] + 1)
                    queue.append((adjacent_x, adjacent_y))
                    
        return rooms
