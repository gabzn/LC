https://leetcode.com/problems/earliest-second-to-mark-indices-i/

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], indices: List[int]) -> int:
        def can_mark_all_in_x_seconds(x):
            latest_sec_to_mark_idx = {}
            
            # Find the latest second to perform any ops on each index starting from 0 to x seconds
            for second in range(x):
                idx_to_mark = indices[second]
                latest_sec_to_mark_idx[idx_to_mark] = second + 1
            
            if len(latest_sec_to_mark_idx) != N:
                return False
            
            # Sort them based on the earliest time. We want to mark indices that have earlier ending time
            latest_sec_to_mark_idx = sorted(latest_sec_to_mark_idx.items(), key=lambda pair: pair[1])        
            total_seconds = 0
            
            # Go through each and find the total seconds needed to mark such idx
            # Seconds needed to mark idx i = the # of opeation one + 1 operation two
            # If the time to mark idx i and all others before it exceeds the latest time to mark idx i, return false 
            for idx, latest_sec in latest_sec_to_mark_idx:
                seconds_needed_to_mark_idx = nums[idx] + 1
                
                total_seconds += seconds_needed_to_mark_idx
                if total_seconds > latest_sec:
                    return False
            
            return True
        
        N, M = len(nums), len(indices)
        
        for i in range(M):
            indices[i] -= 1
        
        left, right = 0, M + 1
        res = -1
        
        # Binary Search on the time
        while left + 1 != right:
            mid = (left + right) // 2
            
            if can_mark_all_in_x_seconds(mid):
                res = mid
                right = mid
            else:
                left = mid
        
        return res
