https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        N = len(nums)
        
        # Store the number of times a certain prefix sum occurs in nums
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        
        res = 0
        running_sum = 0
        
        for idx, num in enumerate(nums):
            running_sum += num
            
            diff = running_sum - goal
            if diff in prefix_count:
                res += prefix_count[diff]
            
            prefix_count[running_sum] += 1
        
        return res
