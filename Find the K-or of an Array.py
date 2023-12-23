https://leetcode.com/problems/find-the-k-or-of-an-array/

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        res = 0
        
        for i in range(32):
            bits_set = 0
            
            for num in nums:
                if num & (2 ** i):
                    bits_set += 1
            
            if bits_set >= k:
                res += (2 ** i)
        
        return res
