https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_dict = {0: -1}
        running_sum = 0
        
        for index, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k
            
            """
            If the same remainder occurs multiple times,
            that means since the first time it occurs, the sum has been incremented by k.
            
            We don't want to update the index where this remainder occurs first.
            When the same remainder occurs multiple times, we can check its current index with 
            its first occurrence index to see if the length is > 1.
            """
            if remainder not in remainder_dict:
                remainder_dict[remainder] = index
            
            if remainder in remainder_dict and index - remainder_dict[remainder] > 1:
                return True
            
        return False
