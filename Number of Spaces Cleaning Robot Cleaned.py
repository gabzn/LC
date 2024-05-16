https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        def is_empty_space(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS and room[x][y] == 0
        
        ROWS, COLS = len(room), len(room[0])
        ROTATIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = 0
        
        visited_directions = set()
        cleaned_cells = set([(0, 0)])
        stack = [(0, 0)]
        
        while stack:
            x, y = stack.pop()
            
            if (x, y, r) in visited_directions:
                return len(cleaned_cells)
            visited_directions.add((x, y, r))
                        
            next_x = x + ROTATIONS[r][0]
            next_y = y + ROTATIONS[r][1]
            
            # Keep going in the same direction
            if is_empty_space(next_x, next_y):
                if (next_x, next_y) not in cleaned_cells:
                    cleaned_cells.add((next_x, next_y))   

                stack.append((next_x, next_y))
                
            # Come back to the current one but this time turn 90 degree clockwise
            else:
                stack.append((x, y))
                r = (r + 1) % 4
        
        return len(cleaned_cells)
----------------------------------------------------------------------------------------
class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        def is_empty_space(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS and room[x][y] == 0
        
        ROWS, COLS = len(room), len(room[0])
        ROTATIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = 0
        visited_directions = set()
        cleaned_cells = set()
        stack = [(0, 0)]
        
        while stack:
            x, y = stack.pop()
            
            if (x, y, r) in visited_directions:
                return len(cleaned_cells)
            visited_directions.add((x, y, r))
            
            if (x, y) not in cleaned_cells:
                cleaned_cells.add((x, y))
            
            offset_x, offset_y = ROTATIONS[r]
            next_x, next_y = x + offset_x, y + offset_y
            
            # Keep going in the same direction
            if is_empty_space(next_x, next_y):
                stack.append((next_x, next_y))
            # Come back to the current one but this time turn 90 degree clockwise
            else:
                stack.append((x, y))
                r = (r + 1) % 4
        
        return len(cleaned_cells)
---------------------------------------------------------------------------------
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
