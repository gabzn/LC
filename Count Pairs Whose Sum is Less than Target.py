https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        N = len(nums)
        res = 0
        
        for r in range(N):
            for l in range(r + 1, N):
                if nums[l] + nums[r] < target:
                    res += 1
                    
        return res
