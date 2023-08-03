https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        LEN = len(nums)
        nums.sort()
        res = set()
        
        for first in range(LEN):
            for second in range(first + 1, LEN):
                third, fourth = second + 1, LEN - 1
                
                while third < fourth:
                    four_sum = nums[first] + nums[second] + nums[third] + nums[fourth]
                    
                    if four_sum == target:
                        res.add((nums[first], nums[second], nums[third], nums[fourth]))
                        third += 1
                    
                    if four_sum < target:
                        third += 1
                    if four_sum > target:
                        fourth -= 1
    
        return res
