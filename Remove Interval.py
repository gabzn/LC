https://leetcode.com/problems/remove-interval/

class Solution:
    def removeInterval(self, intervals: List[List[int]], to_be_removed: List[int]) -> List[List[int]]:        
        r_start, r_end = to_be_removed
        
        res = []
        
        for cur_start, cur_end in intervals:
            # No overlapping
            if cur_start > r_end or cur_end < r_start:
                res.append([cur_start, cur_end])
            else:
                if cur_start >= r_start and cur_end <= r_end:
                    continue
                    
                if cur_start < r_start:
                    new_end = r_start
                    res.append([cur_start, new_end])
                    
                if cur_end > r_end:
                    new_start = r_end
                    res.append([new_start, cur_end])
        
        return res
