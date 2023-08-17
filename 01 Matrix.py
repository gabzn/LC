https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def is_valid_cell_with_value_one(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS and mat[x][y] == 1
        
        ROWS, COLS = len(mat), len(mat[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        visited_cells = set()
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited_cells.add((r, c))
        
        while queue:
            n = len(queue)
            
            for _ in range(n):
                x, y, distance = queue.popleft()
                
                for offset_x, offset_y in DIRECTIONS:
                    adjacent_x, adjacent_y = offset_x + x, offset_y + y
                    
                    if is_valid_cell_with_value_one(adjacent_x, adjacent_y) and (adjacent_x, adjacent_y) not in visited_cells:
                        mat[adjacent_x][adjacent_y] = distance + 1
                        queue.append((adjacent_x, adjacent_y, distance + 1))
                        visited_cells.add((adjacent_x, adjacent_y))
                        
        return mat
