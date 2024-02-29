https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        N = len(points)
        
        points.sort(key=lambda p: (p[0], -p[1]))
        res = 0
        
        for i in range(N):
            highest_y = -inf
            
            for j in range(i + 1, N):
                if points[i][1] >= points[j][1] and points[j][1] > highest_y:
                    res += 1
                    highest_y = points[j][1]
        
        return res
