https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)

        # prefix = [0]
        # for num in nums:
        #     prefix.append(prefix[-1] + num)
        prefix = list(accumulate(nums, initial=0))

        res = -inf
        min_prefix_for_remainder = [inf] * k
        min_prefix_for_remainder[0] = 0

        for R in range(1, N + 1):
            # (R − L) % k = 0
            # R % k = L % k
            r = R % k
            
            res = max(res, prefix[R] - min_prefix_for_remainder[r])
            min_prefix_for_remainder[r] = min(
                min_prefix_for_remainder[r], 
                prefix[R]
            )

        return res
