https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/
https://leetcode.com/problems/range-addition/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:                
        LEN = len(nums)
        MOD = 10 ** 9 + 7
        
        diff = [0] * (LEN + 1)
        for start, end in requests:
            diff[start] += 1
            diff[end + 1] -= 1
        
        for i in range(1, LEN + 1):
            diff[i] += diff[i - 1]

        diff.pop()
        diff.sort(reverse=True)
        nums.sort(reverse=True)
        
        res = 0
        for multiplier, num in zip(diff, nums):
            res += (multiplier * num)
            
        return res % MOD
