https://leetcode.com/problems/majority-element/
  
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        for num, occurrence in counter.items():
            if occurrence > len(nums) // 2:
                return num
