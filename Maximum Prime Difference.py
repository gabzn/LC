https://leetcode.com/problems/maximum-prime-difference/

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True            
        
        N = len(nums)
        
        lst = []        
        for idx, num in enumerate(nums):
            if is_prime(num):
                lst.append(idx)
                
        return lst[-1] - lst[0]
