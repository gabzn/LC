https://leetcode.com/problems/subarray-sums-divisible-by-k/
https://www.youtube.com/watch?v=iABMUwDN6L0

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_counts = defaultdict(int)
        remainder_counts[0] += 1
        running_sum, ans = 0, 0
        
        for num in nums:
            running_sum += num
            
            remainder = running_sum % k
            if remainder in remainder_counts:
                ans += remainder_counts[remainder]
            
            remainder_counts[remainder] += 1

        return ans
-----------------------------------------------------------------------------------------------  
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_counts = {0: 1}
        running_sum, ans = 0, 0
        
        for num in nums:
            running_sum += num
            
            remainder = running_sum % k
            if remainder in remainder_counts:
                ans += remainder_counts[remainder]
                remainder_counts[remainder] += 1
            else:
                remainder_counts[remainder] = 1
            
        return ans
