https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        N = len(profits)
        
        projects = sorted(zip(capital, profits))
        i = 0
        heap = []
        
        for _ in range(k):
            while i < N and projects[i][0] <= w:
                heappush(heap, -projects[i][1])
                i += 1
            
            if len(heap) == 0:
                break
            
            w += -heappop(heap)
        
        return w
