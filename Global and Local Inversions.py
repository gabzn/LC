https://leetcode.com/problems/global-and-local-inversions/

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # The intuition is to find one example where
        # it has more than 2 global inversions.
        
        for i, num in enumerate(nums):
            if abs(i - num) > 1:
                return False
        return True
