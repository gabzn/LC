https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/
https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/discuss/4278166/Simple-Array-Question-oror-Self-Explainatory-Code

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        LEN = len(nums1)
        
        last_of_num1 = nums1[-1]
        last_of_num2 = nums2[-1]
        
        # Don't swap the last digits
        swap1 = 0
        for idx in range(LEN - 1):
            if nums1[idx] <= last_of_num1 and nums2[idx] <= last_of_num2:
                continue
            
            # Check to see if the cur nums can be swapped
            if nums2[idx] <= last_of_num1 and nums1[idx] <= last_of_num2:
                swap1 += 1
            else:
                return -1
        
        # Swap the last digits
        swap2 = 1
        for idx in range(LEN - 1):
            if nums1[idx] <= last_of_num2 and nums2[idx] <= last_of_num1:
                continue

            # Check to see if the cur nums can be swapped
            if nums1[idx] <= last_of_num1 and nums2[idx] <= last_of_num2:
                swap2 += 1
            else:
                return -1
        
        return min(swap1, swap2)    
