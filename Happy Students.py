https://leetcode.com/problems/happy-students/

class Solution:
    def countWays(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        
        res = 1 if nums[0] != 0 else 0
        selected = 0
        
        for i, num in enumerate(nums):
            selected += 1
            
            if selected > num and (i + 1 == N or selected < nums[i + 1]):
                res += 1
        
        return res
