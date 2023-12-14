https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])

        # Find the number of ones and zeros in every single row
        diff = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            counter = Counter(grid[r])
            ones_minus_zeros = counter[1] - counter[0]
            
            for c in range(COLS):
                diff[r][c] = ones_minus_zeros
        
        # Find the number of ones and zeros in every single col
        for c in range(COLS):
            counter = Counter()
            for r in range(ROWS):
                counter[grid[r][c]] += 1
            ones_minus_zeros = counter[1] - counter[0]
            
            for r in range(ROWS):
                diff[r][c] += ones_minus_zeros
         
        return diff   
