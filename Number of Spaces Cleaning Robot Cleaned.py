https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        def is_empty_space(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS and room[x][y] == 0
        
        def dfs(x, y, r):
            if (x, y, r) in visited_cells:
                return len(cleaned_cells)
            
            visited_cells.add((x, y, r))
            cleaned_cells.add((x, y))
            
            offset_x, offset_y = ROTATIONS[r]
            next_x = x + offset_x
            next_y = y + offset_y
            if is_empty_space(next_x, next_y):
                return dfs(next_x, next_y, r)
            
            return dfs(x, y, (r + 1) % 4)
        
        ROWS, COLS = len(room), len(room[0])
        ROTATIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cleaned_cells = set()
        visited_cells = set()
        return dfs(0, 0, 0)
