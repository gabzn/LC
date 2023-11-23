https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        M = len(arrays)
        
        # One observation is that the elements in the middle are irrelevant
        prev_min, prev_max = arrays[0][0], arrays[0][-1]
        res = 0
        
        for i in range(1, M):
            cur_min, cur_max = arrays[i][0], arrays[i][-1]
            res = max(res, abs(cur_max - prev_min), abs(prev_max - cur_min))
            prev_min = min(prev_min, cur_min)
            prev_max = max(prev_max, cur_max)
            
        return res
