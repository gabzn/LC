https://leetcode.com/problems/make-a-square-with-the-same-color/

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for x in range(2):
            for y in range(2):
                count = Counter()
                count[grid[x][y]] += 1
                count[grid[x + 1][y]] += 1
                count[grid[x][y + 1]] += 1
                count[grid[x + 1][y + 1]] += 1
                
                if len(count) == 1:
                    return True
                if count['B'] == 1 and count['W'] == 3:
                    return True
                if count['W'] == 1 and count['B'] == 3:
                    return True
                    
        return False
