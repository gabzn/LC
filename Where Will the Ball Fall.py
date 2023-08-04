https://leetcode.com/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        M, N = len(grid), len(grid[0])
        answer = [-1 for _ in range(N)]
                
        def dfs(x, y):
            stack = [(x, y)]
            res = -1
            
            while stack:
                a, b = stack.pop()
                if a == M:
                    res = b
                    break
                
                # if current cell is 1, check if the cell to the right is -1 or wall
                if grid[a][b] == 1 and (b + 1 == N or grid[a][b+1] == -1):
                    return -1
                    
                # if current cell is -1, check if the cell to the left is 1 or wall
                if grid[a][b] == -1 and (b - 1 == -1 or grid[a][b-1] == 1):
                    return -1
                                
                stack.append((a+1, b+1) if grid[a][b] == 1 else (a+1, b-1))
            return res
        
        for index in range(N):
            answer[index] = dfs(0, index)
        return answer
--------------------------------------------------------------------------------------
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        res = []
        
        """
        The for loop simulates that we are dropping each ball from the top,
        and we'll use dfs to trace the route they are dropping.
        """
        for b in range(C):
            self.dfs(grid, R, C, 0, b, res)

        return res
    
    def dfs(self, grid, R, C, r, c, res):
        # Base case where the ball touches the ground.
        if r == R:
            res.append(c)
            return
        
        # We find where the ball is at right now and look at the value in that cell.
        cur_value = grid[r][c]
        
        # If it's 1, we check if it's right is -1 which will get the ball stuck.
        if cur_value == 1:
            # First check if it is out of bound, then check if the cell to the right will get the ball stuck.
            if c + 1 >= C or cur_value + grid[r][c+1] == 0:
                res.append(-1)
                return
            
            self.dfs(grid, R, C, r+1, c+1, res)
        
        # If it's -1, we check if it's right is 1 which will get the ball stuck.
        if cur_value == -1:
            # First check if it is out of bound, then check if the cell to the left will get the ball stuck.
            if c - 1 < 0 or cur_value + grid[r][c-1] == 0:
                res.append(-1)
                return
            
            self.dfs(grid, R, C, r+1, c-1, res)
