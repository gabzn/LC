https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
  
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
  
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = -1
        
        for ind in range(len(arr)-1, -1, -1):
            cur_num = arr[ind]
            arr[ind] = cur_max
            cur_max = max(cur_max, cur_num)
        
        return arr
