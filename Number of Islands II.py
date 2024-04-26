https://leetcode.com/problems/number-of-islands-ii/

class Solution:
    def numIslands2(self, ROWS: int, COLS: int, positions: List[List[int]]) -> List[int]:
        def is_valid_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS
        
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x = root[x]
            root_y = root[y]
            root[root_y] = root_x
        
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        root = [-1] * (ROWS * COLS)
        for x in range(ROWS):
            for y in range(COLS):
                i = (x * COLS) + y
                root[i] = i
        
        res = []
        visited = set()
        islands = 0
        
        for x, y in positions:
            if (x, y) in visited:
                res.append(islands)
                continue
            
            visited.add((x, y))
            islands += 1
            i = (x * COLS) + y
            
            for offset_x, offset_y in DIRECTIONS:
                next_x = offset_x + x
                next_y = offset_y + y
                j = (next_x * COLS) + next_y
                
                if is_valid_cell(next_x, next_y) and (next_x, next_y) in visited:    
                    if find(i) == find(j):
                        continue
                    
                    union(i, j)
                    islands -= 1
            
            res.append(islands)
            
        return res
