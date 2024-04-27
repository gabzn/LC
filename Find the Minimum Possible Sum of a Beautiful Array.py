https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/
https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/discuss/3965161/O(1)-oror-2-lines-code-oror-understandable-100

class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        MOD = (10 ** 9) + 7
        
        half = target // 2
        if n <= half:
            return ((n * (n + 1)) // 2) % MOD
        
        first_half = (half * (half + 1) // 2)
        diff = n - half
        second_half = ((diff + target) * (diff + target - 1) // 2) - ((target * (target - 1)) // 2)
        return (first_half + second_half) % MOD
