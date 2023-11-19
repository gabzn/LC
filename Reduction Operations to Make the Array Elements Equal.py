https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        LEN = len(nums)
        nums.sort(reverse=True)
        res = 0
        
        for i in range(1, LEN):
            if nums[i - 1] > nums[i]:
                res += i
                    
        return res
