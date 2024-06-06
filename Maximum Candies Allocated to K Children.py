https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can_distribute_mid_candies(x):        
            count = 0
            for c in candies:
                count += (c // x)
            return count >= k
        
        left = -1
        right = 10 ** 8
        
        while left + 1 != right:
            mid = (left + right) // 2
            if mid == 0:
                return 0
            
            if can_distribute_mid_candies(mid):
                left = mid
            else:
                right = mid
        
        return left
