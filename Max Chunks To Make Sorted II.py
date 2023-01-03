https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
  
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Make a sorted version of arr and compare each digit.
        If the digits at the current indices are the same, that means it can be a chunk itself.
        
        If the digits are not the same, but the current running sums are the same. That means sorting this part could make a chunk.
        """
        sorted_arr = sorted(arr.copy())
        unsorted_sum, sorted_sum, res = 0, 0, 0
        
        for num_sorted, num_unsorted in zip(sorted_arr, arr):
            sorted_sum += num_sorted
            unsorted_sum += num_unsorted
            
            if sorted_sum == unsorted_sum:
                res += 1
                sorted_sum = 0
                unsorted_sum = 0
        
        return res
