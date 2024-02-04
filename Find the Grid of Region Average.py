https://leetcode.com/problems/find-the-grid-of-region-average/

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        def is_in_bound(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS

        def calculate_region(start_x, start_y, end_x, end_y):
            total = 0

            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    for offset_x, offset_y in DIRECTIONS:
                            next_x, next_y = offset_x + x, offset_y + y

                            if start_x <= next_x <= end_x and start_y <= next_y <= end_y:
                                diff = abs(image[x][y] - image[next_x][next_y])
                                if diff > threshold:
                                    return False, -1

                    total += image[x][y]

            return True, total
        
        ROWS, COLS = len(image), len(image[0])
        DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
                
        g = [[[0, 0] for _ in range(COLS)] for _ in range(ROWS)]
        for start_x in range(ROWS):
            for start_y in range(COLS):
                end_x = start_x + 3 - 1
                end_y = start_y + 3 - 1
                if not is_in_bound(end_x, end_y):
                    break
                
                is_a_region, total_sum_in_the_region = calculate_region(start_x, start_y, end_x, end_y)
                if is_a_region:
                    for x in range(start_x, end_x + 1):
                        for y in range(start_y, end_y + 1):
                            g[x][y][0] += total_sum_in_the_region // 9
                            g[x][y][1] += 1 
                    
        res = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for x in range(ROWS):
            for y in range(COLS):
                if g[x][y][1] == 0:
                    res[x][y] = image[x][y]
                else:
                    res[x][y] = g[x][y][0] // g[x][y][1]
        
        return res
