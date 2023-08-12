https://leetcode.com/problems/teemo-attacking/

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        LEN = len(timeSeries)
        if LEN == 0:
            return 0
        
        total = duration
        for index in range(LEN - 1):
            total += min(timeSeries[index + 1] - timeSeries[index], duration)
        
        return total
