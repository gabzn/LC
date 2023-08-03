https://leetcode.com/problems/3sum-smaller/

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        LEN = len(nums)
        nums.sort()
        res = 0
        
        for index in range(LEN):
            l, r = index + 1, LEN - 1
            
            while l < r:
                three_sum = nums[index] + nums[l] + nums[r]
                
                if three_sum >= target:
                    r -= 1
                else:
                    res += r - l
                    l += 1
        
        return res  
