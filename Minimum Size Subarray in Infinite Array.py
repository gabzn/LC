https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        N = len(nums)
        total = sum(nums)
        quotient, remainder = divmod(target, total)
        
        nums += nums
        min_len = inf
        cur = 0
        left = 0
        for right in range(len(nums)):
            cur += nums[right]
            
            while cur > remainder:
                cur -= nums[left]
                left += 1
            
            if cur == remainder:
                min_len = min(min_len, right - left + 1)
        
        return -1 if min_len == inf else quotient * N + min_len
---------------------------------------------------------------------------------
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        N = len(nums)
        total = sum(nums)
        quotient, remainder = divmod(target, total)

        min_len = inf
        cur = 0
        left = 0

        for right in range(2 * N):
            cur += nums[right % N]

            while cur > remainder:
                cur -= nums[left % N]
                left += 1

            if cur == remainder:
                min_len = min(min_len, right - left + 1)

        return -1 if min_len == inf else quotient * N + min_len
