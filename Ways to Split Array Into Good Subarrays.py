https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/
https://www.youtube.com/watch?v=aLzp4jf9HCw

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        LEN, MOD = len(nums), ((10**9) + 7)
        i, res = 0, 1
        is_first_one = True
        
        while i < LEN:
            count_of_zeroes = 0
            
            while i < LEN and nums[i] == 0:
                count_of_zeroes += 1
                i += 1
            
            if i == LEN:
                break
            
            if is_first_one:
                is_first_one = False
            else:
                res = (res * (count_of_zeroes + 1)) % MOD
            
            i += 1
        
        if is_first_one:
            return 0
        return res
