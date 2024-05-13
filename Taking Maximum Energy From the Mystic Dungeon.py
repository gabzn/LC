leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        N = len(energy)
        res = -inf
        
        for i in range(N - 1, -1, -1):
            if i + k < N:
                energy[i] += energy[i + k]
            res = max(res, energy[i])        
        
        return res
