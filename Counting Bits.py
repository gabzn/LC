https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_one_bits(x):
            one_bits = 0
            
            while x != 0:
                x &= x - 1
                one_bits += 1
            
            return one_bits
        
        ans = [0]
        for i in range(1, n + 1):
            ans.append(count_one_bits(i))
    
        return ans
