https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split_nums_into_subarrays_where_each_sum_is_at_most_mid(mid):
            splits = running_sum = 0

            for num in nums:
                if running_sum + num <= mid:
                    running_sum += num 
                else:
                    splits += 1
                    running_sum = num
 
            return splits + 1 <= k

        left, right = max(nums) - 1, sum(nums) + 1
        
        while left + 1 != right:
            mid = (left + right) // 2
            
            if can_split_nums_into_subarrays_where_each_sum_is_at_most_mid(mid):
                right = mid
            else:
                left = mid
    
        return right
