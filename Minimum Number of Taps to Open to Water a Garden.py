https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """
        Visualizing the intervals helps!
        Be greedy and always pick the interval that covers more area
        """
        max_reach = [0] * (n + 1)        
        
        for i in range(n + 1):
            dist = ranges[i]
            
            left = max(0, i - dist)
            right = min(n, i + dist)
            
            max_reach[left] = max(max_reach[left], right)
        
        res, cur_end, next_end = 0, 0, 0
        
        for i in range(n + 1):
            if i > next_end:
                return -1
            
            if i > cur_end:
                res += 1
                cur_end = next_end
            
            next_end = max(next_end, max_reach[i])
        
        return res
