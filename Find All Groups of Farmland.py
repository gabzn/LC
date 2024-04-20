https://leetcode.com/problems/find-all-groups-of-farmland/

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def is_valid_land(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS and land[x][y] == 1
        
        def bfs(r, c):
            queue = deque([(r, c)])
            end = []
            while queue:
                x, y = queue.popleft()
                end = [x, y]
                
                for offset_x, offset_y in DIRECTIONS:
                    next_x = offset_x + x
                    next_y = offset_y + y
                    if is_valid_land(next_x, next_y):
                        land[next_x][next_y] = 0
                        queue.append((next_x, next_y))
            return end
            
        ROWS, COLS = len(land), len(land[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        res = []
        for x in range(ROWS):
            for y in range(COLS):
                if land[x][y] == 1:
                    land[x][y] = 0
                    group = [x, y] + bfs(x, y)
                    res.append(group)
                    
        return res
