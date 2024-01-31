https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

class Solution:
    def maxValue(self, n: int, index: int, max_sum: int) -> int:
        def compute_sequence_sum_from_one_to_x(x):
            return (x * (x + 1)) // 2
        
        def is_setting_index_to_target_valid(target):
            total = 0
            
            # left
            if target > left_len:
                total += compute_sequence_sum_from_one_to_x(target) - compute_sequence_sum_from_one_to_x(target - left_len)
            else:
                total += compute_sequence_sum_from_one_to_x(target) + (left_len - target)
            
            # right
            if target > right_len:
                total += compute_sequence_sum_from_one_to_x(target) - compute_sequence_sum_from_one_to_x(target - right_len)
            else:
                total += compute_sequence_sum_from_one_to_x(target) + (right_len - target)
                 
            return total - target <= max_sum
        
        left_len = index + 1
        right_len = n - index
        
        left, right = 0, max_sum + 1
        
        while left + 1 != right:
            mid = (left + right) // 2
            
            if is_setting_index_to_target_valid(mid):
                left = mid
            else:
                right = mid
        
        return left
