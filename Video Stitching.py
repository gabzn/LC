https://leetcode.com/problems/video-stitching/

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        
        LEN = len(clips)
        res, cur_end, index = 0, 0, 0
        
        while index < LEN:
            next_end = cur_end
            
            # If current start <= cur_end, find the next_end
            while index < LEN and clips[index][0] <= cur_end:
                next_end = max(clips[index][1], next_end)
                index += 1
            
            # Increment the count and update cur_end to next_end
            res += 1
            cur_end = next_end
            if cur_end >= time:
                return res
            
            # If index reaches the end or cur_end can never reach next_start, return -1
            if index == LEN or cur_end < clips[index][0]:
                return -1
-----------------------------------------------------------------------------------------------  
