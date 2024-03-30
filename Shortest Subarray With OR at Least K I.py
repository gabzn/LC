https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = inf
        for i in range(N):
            num1 = nums[i]
            if num1 >= k:
                return 1
            
            for j in range(i + 1, N):
                num1 = num1 | nums[j]
                if num1 >= k:
                    res = min(res, j - i + 1)
                        
        return res if res != inf else -1
