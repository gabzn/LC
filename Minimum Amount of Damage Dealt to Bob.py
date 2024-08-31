https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        N = len(damage)

        rounds = [ceil(h / power) for h in health]
        ratios = sorted([ (damage[i] / rounds[i], i) for i in range(N) ], reverse=True)         
        total_damage_per_round = sum(damage)

        res = 0
        for _, i in ratios:
            res += total_damage_per_round * rounds[i]
            total_damage_per_round -= damage[i]    
        return res
