https://leetcode.com/problems/maximum-score-of-a-good-subarray/
https://www.youtube.com/watch?v=OcqPeux47fU

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        LEN = len(nums)
        res, min_val = 0, nums[k]
        i = j = k
        
        while i >= 0 and j < LEN:
            
            # Try moving i to the left and j to the right
            while i > 0 and nums[i - 1] >= min_val:
                i -= 1
            while j < LEN - 1 and nums[j + 1] >= min_val:
                j += 1

            # Update res
            res = max(res, min_val * (j - i + 1))
            
            # Stop when both i and j are at the end
            if i == 0 and j == LEN - 1:
                break
            
            # Check both sides to see where to expand
            if i > 0 and j < LEN - 1:
                if nums[i - 1] >= nums[j + 1]:
                    i -= 1
                    min_val = nums[i]
                else:
                    j += 1
                    min_val = nums[j]    
                continue
                
            if i > 0:
                i -= 1
                min_val = nums[i]
            else:
                j += 1
                min_val = nums[j]
                
        return res
