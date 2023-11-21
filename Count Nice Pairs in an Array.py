https://leetcode.com/problems/count-nice-pairs-in-an-array/

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        def rev(num):
            rev_num = 0
            
            while num > 0:
                num, last_digit = divmod(num, 10)
                rev_num = rev_num * 10 + last_digit
                    
            return rev_num
            
        m = {}
        res = 0
        
        for num in nums:
            rev_num = rev(num)
            diff = num - rev_num
            
            if diff in m:
                res += m[diff] 
                m[diff] += 1
            else:
                m[diff] = 1
            
        return res % MOD
