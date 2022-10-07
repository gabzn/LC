https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
  
 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return 1, 2
        
        # Since the list is sorted, we can have 2 pointers pointing at the beginning and the end.
        # If the beginning + the end is greater than the target, we know we should decrement the right pointer by 1
        # If the beginning + the end is smaller than the target, we need to increment the left pointer by 1
        l, r = 0, len(numbers) - 1
        while True:
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] == target:
                return l+1, r+1
