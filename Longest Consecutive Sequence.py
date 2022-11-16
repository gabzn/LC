https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
  
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        
        for num in nums:
            
            """
            We want to know whether the num we are looking at is the start of the subsequence or not.
            If a num is the start of a subsequence, num - 1 does not exist.
            """
            if num - 1 not in num_set:
                subsequence_len = 1
                
                while num + subsequence_len in num_set:
                    subsequence_len += 1
                
                res = max(res, subsequence_len)
                
        return res
