https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        total = 0
        counter = Counter()

        for i, num in enumerate(nums):
            total += num
            counter[num] += 1

            if i + 1 - k < 0:
                continue

            if len(counter) == k:
                res = max(res, total)
            
            leftmost_num = nums[i + 1 - k]
            total -= leftmost_num

            counter[leftmost_num] -= 1
            if counter[leftmost_num] == 0:
                del counter[leftmost_num]

        return res
