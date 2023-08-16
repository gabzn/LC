https://leetcode.com/problems/the-maze-ii/

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        def is_empty_space(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS and maze[x][y] == 0
            
        ROWS, COLS = len(maze), len(maze[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        START_X, START_Y = start
        END_X, END_Y = destination
        
        distances = [[math.inf for _ in range(COLS)] for _ in range(ROWS)]
        distances[START_X][START_Y] = 0    
        
        heap = [(0, START_X, START_Y)]
        while heap:
            distance, x, y = heappop(heap)
            
            for offset_x, offset_y in DIRECTIONS:
                adjacent_x, adjacent_y = x + offset_x, y + offset_y
                rolling_distance = 1
                
                while is_empty_space(adjacent_x, adjacent_y):
                    adjacent_x += offset_x
                    adjacent_y += offset_y
                    rolling_distance += 1    
                
                adjacent_x -= offset_x
                adjacent_y -= offset_y
                rolling_distance -= 1
                
                if distances[x][y] + rolling_distance < distances[adjacent_x][adjacent_y]:
                    distances[adjacent_x][adjacent_y] = distances[x][y] + rolling_distance
                    heappush(heap, (rolling_distance + distance, adjacent_x,adjacent_y))     
                    
        return distances[END_X][END_Y] if distances[END_X][END_Y] != math.inf else -1
