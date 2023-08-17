https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def is_valid_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS
        
        def bfs(queue, visited_cells):
            while queue:
                x, y = queue.popleft()
                
                for offset_x, offset_y in DIRECTIONS:
                    adjacent_x, adjacent_y = offset_x + x, offset_y + y
                    
                    if is_valid_cell(adjacent_x, adjacent_y) and heights[adjacent_x][adjacent_y] >= heights[x][y] and (adjacent_x, adjacent_y) not in visited_cells:
                        visited_cells.add((adjacent_x, adjacent_y))
                        queue.append((adjacent_x, adjacent_y))        

        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        queue_for_pacific, queue_for_atlantic = deque(), deque()
        visited_cells_for_pacific, visited_cells_for_atlantic = set(), set()
        
        # Start from the edge cells and see where they can flow to
        for index in range(COLS):
            queue_for_pacific.append((0, index))
            visited_cells_for_pacific.add((0, index))
            
            queue_for_atlantic.append((ROWS - 1, index))
            visited_cells_for_atlantic.add((ROWS - 1, index))
            
        for index in range(ROWS):
            queue_for_pacific.append((index, 0))
            visited_cells_for_pacific.add((index, 0))
            
            queue_for_atlantic.append((index, COLS - 1))
            visited_cells_for_atlantic.add((index, COLS - 1))
        
        bfs(queue_for_pacific, visited_cells_for_pacific)
        bfs(queue_for_atlantic, visited_cells_for_atlantic)
        
        return visited_cells_for_pacific.intersection(visited_cells_for_atlantic)    
