https://leetcode.com/problems/count-the-number-of-good-subarrays/
https://www.youtube.com/watch?v=k3ctPuOQJr4

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        freq = Counter()
        res = pairs = 0
        left = right = 0
        
        while left < N:    
            while right < N and pairs < k:
                right_num = nums[right]                
                pairs += freq[right_num]
                freq[right_num] += 1
                right += 1
                
            if pairs >= k:
                res += (N - right) + 1
            
            left_num = nums[left]
            freq[left_num] -= 1
            pairs -= freq[left_num]
            left += 1
        
        return res
