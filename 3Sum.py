https://leetcode.com/problems/3sum/
  
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
AKA: 3 different-indexed numbers add up to 0.
  
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        res = []
        
        for ind in range(len(nums)):
            """
            Only perform binary search if ind == 0 meaning the first num
            or the previous num is not the same.
            [-2, -2, -2, 0, 0, 4, 4]
                 ind
            We don't want to look at the current ind becasue we've already found 
            solutions using ind-1.
            """
            if (ind == 0) or (nums[ind] != nums[ind-1]):
                
                l, r = ind+1, len(nums)-1
                while l < r:
                    three_sum = nums[ind] + nums[l] + nums[r]

                    if three_sum > 0:
                        r -= 1
                    if three_sum < 0:
                        l += 1
                    if three_sum == 0:
                        # Found one solution.
                        res.append([nums[ind], nums[l], nums[r]])
                        """
                        For each nums[ind], we want to know if there's any more solutions using nums[ind],
                        but at the same time, we want to avoid having the same triplets.
                        [-2, -2, -2, 0, 0, 4, 4]
                         ind  l               r
                        [-2, -2, 4] is a solution, so we want to skip the third -2 as well as the second to last 4.
                        """
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                            
                        l += 1
                        r -= 1
            
        return res
