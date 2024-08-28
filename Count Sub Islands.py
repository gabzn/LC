https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def is_valid_cell(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS

        def bfs(r, c):
            queue = deque([(r, c)])
            grid2[r][c] = 0
            is_sub_island = True

            while queue:
                x, y = queue.popleft()
                if grid1[x][y] != 1:
                    is_sub_island = False

                for offset_x, offset_y in DIRECTIONS:
                    next_x = offset_x + x
                    next_y = offset_y + y

                    if is_valid_cell(next_x, next_y) and grid2[next_x][next_y] == 1:
                            queue.append((next_x, next_y))
                            grid2[next_x][next_y] = 0

            return is_sub_island

        ROWS = len(grid1)
        COLS = len(grid1[0])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1 and grid1[r][c] == 1:
                    if bfs(r, c):
                        res += 1
        return res
