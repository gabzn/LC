https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution:
    def minCost(self, colors: str, time_needed: List[int]) -> int:
        LEN = len(colors)
        
        res = prev_idx = 0
        
        for cur_idx in range(1, LEN):            
            # If current color is the same is previous color, remove the one that takes less time
            # If the previous one is removed, update its index to the current one
            if colors[cur_idx] == colors[prev_idx]:
                if time_needed[prev_idx] <= time_needed[cur_idx]:
                    res += time_needed[prev_idx]
                    prev_idx = cur_idx
                else:
                    res += time_needed[cur_idx]
            # If they have different colors, update prev to current index
            else:
                prev_idx = cur_idx
        
        return res
