https://leetcode.com/problems/max-chunks-to-make-sorted/

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        
        for num in arr:
            if len(stack) == 0 or stack[-1] < num:
                stack.append(num)
                continue

            max_element_in_current_chunk = -1
            while stack and stack[-1] > num:
                max_element_in_current_chunk = max(max_element_in_current_chunk, stack.pop())
            stack.append(max_element_in_current_chunk)
        
        return len(stack)
-------------------------------------------------------
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        unsorted_sum, sorted_sum, res = 0, 0, 0
        
        for num_sorted, num_unsorted in zip(sorted_arr, arr):
            sorted_sum += num_sorted
            unsorted_sum += num_unsorted
            
            if sorted_sum == unsorted_sum:
                res += 1
                sorted_sum = 0
                unsorted_sum = 0
        
        return res
