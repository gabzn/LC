https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        l, r, res = [1] * LEN, [1] * LEN, [1] * LEN
        
        for index in range(1, LEN):
            l[index] = nums[index - 1] * l[index - 1]
        
        for index in reversed(range(LEN - 1)):
            r[index] = nums[index + 1] * r[index + 1]
        
        for index in range(LEN):
            res[index] = l[index] * r[index]
        
        return res
