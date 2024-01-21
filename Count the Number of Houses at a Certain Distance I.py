https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        distances = [[inf if i != j else 0 for j in range(n)] for i in range(n)]
        
        if x != y:
            distances[x - 1][y - 1] = 1
            distances[y - 1][x - 1] = 1
                  
        for i in range(2, n + 1):
            distances[i - 1][i - 2] = 1
            distances[i - 2][i - 1] = 1
        
        # Floyd-Warsall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
                                    
        res = [0] * n
        
        for dis in chain(*distances):
            if dis != 0:
                res[dis - 1] += 1
                
        return res
