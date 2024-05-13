https://leetcode.com/problems/score-after-flipping-matrix/

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                grid[r][c] = str(grid[r][c])
        
        # Go through each row and check if flipping 
        # the bits will result in bigger number
        for r in range(ROWS):
            row = grid[r]
            before_str = ''.join(row)
            before_val = int(before_str, 2)
            
            after_str = ''
            after_val = 0
            for digit in row:
                after_str += '1' if digit == '0' else '0'
            after_val = int(after_str, 2)
            
            if after_val > before_val:
                for c in range(COLS):
                    row[c] = after_str[c]
        
        # Go through each col and count the number of 1's and 0's
        # If there are more 0's, flip the column
        for c in range(COLS):
            counter = Counter()
            for r in range(ROWS):
                counter[grid[r][c]] += 1
            
            if counter['1'] < counter['0']:
                zero_count = counter['0']
                for r in range(ROWS):
                    if grid[r][c] == '1':
                        grid[r][c] = '0'
                    else:
                        if zero_count != 0:
                            grid[r][c] = '1'
                            zero_count -= 1
        
        res = 0
        for row in grid:
            res += int(''.join(row), 2)
        
        return res
