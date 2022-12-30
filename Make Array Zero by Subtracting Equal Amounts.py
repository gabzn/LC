https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
  
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num != 0 and num not in s:
                s.add(num)
                
        return len(s)
