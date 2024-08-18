https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:        
        streak = 1
        res = []
        
        for i, num in enumerate(nums):
            if i and nums[i] == nums[i - 1] + 1:
                streak += 1
            else:
                streak = 1
            
            if i + 1 >= k:
                res.append(nums[i] if streak >= k else -1)
        
        return res
