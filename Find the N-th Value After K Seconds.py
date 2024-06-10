https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        
        nums = [1] * n
        while k:
            for i in range(1, n):
                nums[i] += nums[i-1]
            k -= 1
        
        return nums[-1] % MOD
