https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(x):
            digits = [int(d) for d in str(x)]
            max_d = max(digits)
            
            res = 0
            for _ in range(len(digits)):
                res *= 10
                res += max_d
            
            return res
            
        res = 0
        
        for num in nums:
            res += encrypt(num)
        
        return res
