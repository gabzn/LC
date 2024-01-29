https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

class Solution:
    def numOfSubarrays(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7        
        """
        odd + even = odd
        odd - even = odd
        even + odd = odd
        even - odd = odd
        """
        res = 0
        odd_num = even_num = running_sum = 0
        
        for num in nums:
            """
            If the current running sum is odd, 
                we want to know how many even numbers there are before 
                the current num because odd - even = odd. 
            
            Current sum - any even number before will result in subarray of odd sum
            """
            running_sum += num
            if running_sum % 2 == 1:
                res += 1   # + 1 to include the current number
                res += even_num
                odd_num += 1
            else:
                res += odd_num
                even_num += 1
            
        return res % MOD
