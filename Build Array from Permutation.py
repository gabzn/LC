https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        ans = [0] * LEN
        
        for index in range(LEN):
            ans[index] = nums[nums[index]]
            
        return ans
