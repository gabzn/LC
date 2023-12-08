https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        LEN = len(nums)

        bit_and = nums[0]
        for idx in range(LEN):
            bit_and &= nums[idx]
        
        # The minimum score will always be the bitwise AND of all elements
        # If the sum is 0, that means we could have more splits.
        if bit_and > 0:
            return 1

        res = i = 0
        while i < LEN:
            j = i
            cur_num = nums[j]

            while j < LEN and cur_num != 0:
                j += 1
                if j < LEN:
                    cur_num &= nums[j]
            
            if cur_num == 0:
                res += 1
            
            i = j + 1
        
        return res
