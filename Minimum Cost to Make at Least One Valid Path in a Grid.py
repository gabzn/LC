https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:        
        def is_valid_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS
        
        def need_modify_to_reach(x1, y1, x2, y2):
            d = grid[x1][y1]
            offset_x, offset_y = DIRECTIONS[d]
            return (
                x1 + offset_x != x2
                or
                y1 + offset_y != y2
            )
                
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }

        distances = [[inf for _ in range(COLS)] for _ in range(ROWS)]
        distances[0][0] = 0

        heap = [(0, 0, 0)]
        while heap:
            distance, x, y = heappop(heap)
            if distance > distances[x][y]:
                continue
            
            for _, (offset_x, offset_y) in DIRECTIONS.items():
                next_x = x + offset_x
                next_y = y + offset_y
                if is_valid_cell(next_x, next_y):
                    new_distance = distance + 1 if need_modify_to_reach(x, y, next_x, next_y) else distance
                    if new_distance < distances[next_x][next_y]:
                        distances[next_x][next_y] = new_distance
                        heappush(heap, (new_distance, next_x, next_y))

        return distances[-1][-1]
