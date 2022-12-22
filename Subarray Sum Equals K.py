https://leetcode.com/problems/subarray-sum-equals-k/
  
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_dict = {0: 1}
        running_sum, ans = 0, 0
        
        for num in nums:
            running_sum += num
            
            difference = running_sum - k
            if difference in prefix_dict:
                ans += prefix_dict[difference]
            
            if running_sum in prefix_dict:
                prefix_dict[running_sum] += 1
            else:
                prefix_dict[running_sum] = 1
                
        return ans
