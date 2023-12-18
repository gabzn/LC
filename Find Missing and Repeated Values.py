https://leetcode.com/problems/find-missing-and-repeated-values/

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        
        ans = [0, 0]
        visited = set()        
        
        # Find ans[0]
        for r in range(N):
            for c in range(N):
                if grid[r][c] in visited:
                    ans[0] = grid[r][c]
                
                visited.add(grid[r][c])
        
        # Find ans[1] 
        for num in range(1, (N * N) + 1):
            if num not in visited:
                ans[1] = num
                break
                
        return ans
