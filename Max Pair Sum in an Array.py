https://leetcode.com/problems/max-pair-sum-in-an-array/

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        digit_map = {}
        res = -1
        
        for num in nums:
            num_str = str(num)
            max_digit = max(num_str)
            
            # Two-sum inspired approach
            # If the same max digit already showed up once, 
            #   we add the number that has the same max digit and update it 
            # Else 
            #   we put this max digit with this num
            if max_digit in digit_map:
                res = max(res, num + digit_map[max_digit])
                digit_map[max_digit] = max(num, digit_map[max_digit])
            else:
                digit_map[max_digit] = num
            
        return res
