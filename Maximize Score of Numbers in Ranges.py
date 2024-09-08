https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        def ok(m):
            prev = start[0]
            for i in range(1, N):
                meet = prev + m
                if meet > start[i] + d:
                    return False
                prev = max(start[i], meet)
            return True
        
        N = len(start)
        start.sort()
        left = -1
        right = 10 ** 12
        
        while left + 1 != right:
            mid = (left + right) // 2
            
            if ok(mid):
                left = mid
            else:
                right = mid

        return left
