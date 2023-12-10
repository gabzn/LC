https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        LEN = len(nums)
        
        counter = defaultdict(int)
        res = left = 0
        
        for right, num in enumerate(nums):
            counter[num] += 1
            
            while counter[num] > k:
                counter[nums[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
