https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
https://www.youtube.com/watch?v=QGsQtnAXkuk

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        N = len(nums)
        diff_map, res = {}, 0
        
        for index in range(1, N):
            nums[index] += nums[index - 1]
                            
        for index in range(N):
            cur_sum = nums[index]
            if cur_sum == k:
                res = index + 1
            
            diff = cur_sum - k
            if diff in diff_map:
                res = max(res, index - diff_map[diff])
            
            if cur_sum not in diff_map:
                diff_map[cur_sum] = index
            
        return res
