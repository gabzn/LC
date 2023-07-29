https://leetcode.com/problems/can-i-win/
https://leetcode.com/problems/can-i-win/discuss/2826565/Top-down-memopython-simple-solution

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        nums = [num for num in range(1, maxChoosableInteger + 1)]
        if sum(nums) < desiredTotal:
            return False
        
        def dp(nums, remaining, memo):
            if nums[-1] >= remaining:
                return True
            
            tuple_nums = tuple(nums)
            if tuple_nums in memo:
                return memo[tuple_nums]
            
            memo[tuple_nums] = False
            
            for index in range(len(nums)):
                if not dp(nums[:index] + nums[index+1:], remaining - nums[index], memo):
                    memo[tuple_nums] = True
                    return True
            
            return False
        
        return dp(nums, desiredTotal, {})
