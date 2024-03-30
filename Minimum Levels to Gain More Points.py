https://leetcode.com/problems/minimum-levels-to-gain-more-points/

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        N = len(possible)
        
        if possible[0] == 0:
            possible[0] = -1
        
        for i in range(1, N):
            if possible[i] == 0:
                possible[i] = -1
            
            possible[i] += possible[i-1]
                
        for i in range(N - 1):
            if possible[i] > possible[-1] - possible[i]:
                return i + 1
        
        return -1
