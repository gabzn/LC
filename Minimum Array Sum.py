https://leetcode.com/problems/minimum-array-sum/

class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        @cache
        def dp(i, op1, op2):
            if i == N:
                return 0

            skip = do_op1 = do_op2 = do_both = inf
            skip = dp(i + 1, op1, op2) + nums[i]

            if op1 > 0:
                do_op1 = dp(i + 1, op1 - 1, op2) + ((nums[i] + 1) // 2)
            if op2 > 0 and nums[i] >= k:
                do_op2 = dp(i + 1, op1, op2 - 1) + (nums[i] - k)
            if op1 > 0 and op2 > 0 and nums[i] >= k:
                do_both = dp(i + 1, op1 - 1, op2 - 1)
                
                # Subtraction first, then divide by 2
                s = nums[i] - k
                s = (s + 1) // 2
                
                # Division first, then subtract by k
                d = (nums[i] + 1) // 2
                d -= (k if (d >= k) else 0)
                
                do_both += min(s, d)

            return min(skip, do_op1, do_op2, do_both)

        N = len(nums)
        return dp(0, op1, op2)
