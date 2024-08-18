https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

class Solution:
    def maxEnergyBoost(self, A: List[int], B: List[int]) -> int:
        N = len(A)
                
        a = A[0]
        b = B[0]
        
        for i in range(1, N):
            aa = A[i] + a
            bb = B[i] + b
            skip = max(a, b)
            
            a = max(aa, skip)
            b = max(bb, skip)
        
        return max(a, b)
