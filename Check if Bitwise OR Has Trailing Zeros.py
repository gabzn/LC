https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        LEN = len(nums)
        
        for i in range(LEN):
            for j in range(i + 1, LEN):
                or_result = nums[i] | nums[j]
                
                if bin(or_result)[-1] == '0':
                    return True

        return False
