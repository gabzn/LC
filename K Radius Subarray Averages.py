https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        WINDOW_SIZE = 2 * k + 1

        res = [-1] * N
        running_sum = 0

        for i, num in enumerate(nums):
            # Update
            running_sum += num
            
            # Skip if window is not wide enough
            if i + 1 - WINDOW_SIZE < 0:
                continue
            
            # Compute result
            avg = running_sum // WINDOW_SIZE
            res[i - k] = avg

            # Remove leftmost
            running_sum -= nums[i - (2 * k)]

        return res
