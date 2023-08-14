https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        LEN = len(nums)
            
        def dp(index, memo):
            if index < 0:
                return True
            if index in memo:
                return memo[index]
            
            first_condition = nums[index] == nums[index - 1] and dp(index - 2, memo)
            second_condition = nums[index] == nums[index - 1] == nums[index - 2] and dp(index - 3, memo)
            third_condition = nums[index] == nums[index - 1] + 1 == nums[index - 2] + 2 and dp(index - 3, memo)
            
            memo[index] = first_condition or second_condition or third_condition
            return memo[index]
                    
        return dp(LEN - 1, {})
