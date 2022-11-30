https://leetcode.com/problems/unique-number-of-occurrences/
  
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
  
  
from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence_set = set()
        occurence_dict = defaultdict(int)
        
        # Find the number of occurrences of each element.
        for num in arr:
            occurence_dict[num] += 1
        
        # Iterate through the dict and check if there is a repeated value.
        for num in occurence_dict:
            if occurence_dict[num] in occurence_set:
                return False
            occurence_set.add(occurence_dict[num])
            
        return True
