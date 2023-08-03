https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        LEN = len(nums)
        nums.sort()
        res, difference = 0, math.inf
        
        for index in range(LEN):
            num = nums[index]
            
            l, r = index + 1, LEN - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum == target:
                    return target
                
                if abs(three_sum - target) < difference:
                    difference = abs(three_sum - target)
                    res = three_sum
                
                if three_sum > target:
                    r -= 1
                else:
                    l += 1
                
        return res
