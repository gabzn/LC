https://leetcode.com/problems/longest-increasing-subsequence/
  
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Every num itself is a increasing subsequence of length 1
        So we fill out a dp array of size 1
        Start looping through num from the second index,
            if current num is greater than any num prior to it, we want to know if adding current num to prior num will make a longer sequence.
        """
        dp = [1] * len(nums)
        max_len = 1
        
        for right in range(1, len(nums)):
            for left in range(0, right):
                if nums[left] < nums[right]:
                    dp[right] = max(dp[right], 1 + dp[left])
                    max_len = max(max_len, dp[right])
        
        return max_len 
-----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Every num itself is a increasing subsequence of length 1
        So we fill out a dp array of size 1
        Find the longest subsequence from backwards.
        """
        longest_subsequence_for_each_num = [1] * len(nums)
        max_len = 1
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    longest_subsequence_for_each_num[i] = max(longest_subsequence_for_each_num[i], 1 + longest_subsequence_for_each_num[j])
                    max_len = max(max_len, longest_subsequence_for_each_num[i])
        
        return max_len
