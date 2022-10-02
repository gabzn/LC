https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
  
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        # Use a dict to keep track of the apperances of the digits
        num_apperances = defaultdict(int)
        for num in nums:
            num_apperances[num] += 1
            
        # Use a list to keep track of the digits that shows up 1 times, 2 times, 3 times etc...
        # The maximum number of times a digit can show up is equal to the length of the list. 
        # For example: [1,1,1,1,1] where the digit 1 shows up 5 times.
        # The length of the list has to be len(nums) + 1 because it's 0-indexed.
        apperance_list = [[] for _ in range(len(nums) + 1)] 
        for key, value in num_apperances.items():
            apperance_list[value].append(key)
        
        
        for i in range(len(nums), 0, -1):
            if apperance_list[i]:
                res.extend(apperance_list[i])
                
                k -= len(apperance_list[i])
                if not k:
                    return res
