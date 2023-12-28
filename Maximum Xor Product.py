https://leetcode.com/problems/maximum-xor-product/

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        x = 0
        a_xor = a
        b_xor = b
        
        for i in range(n - 1, -1, -1):
            i_bit = 1 << i
            
            # Get the current bits at a and b
            a_bit = a & i_bit
            b_bit = b & i_bit
            
            # If both bits are 0's, set the current bit in x to 1
            if not a_bit and not b_bit:
                x |= i_bit
                continue
            
            # If both bits are 1's, leave the current bit in x to 0
            if a_bit and b_bit:
                continue
            
            # All other cases, we minimize the max between a_xor and b_xor
            # If a is greater and a_bit is one, we want to minimize it by setting it off (1 -> 0)
            # and maximize the smaller one by turning the bit on (0 -> 1)
            if a_xor > b_xor:
                if a_bit:
                    a_xor ^= i_bit
                    b_xor ^= i_bit
                    x |= i_bit
            else:
                if b_bit:
                    a_xor ^= i_bit
                    b_xor ^= i_bit
                    x |= i_bit
        
        return ((a ^ x) * (b ^ x)) % MOD 
