https://leetcode.com/problems/minimum-health-to-beat-game/
  
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        if not armor:
            return sum(damage) + 1
        
        total_damage = sum(damage)
        max_damage = max(damage)
        
        if armor >= max_damage:
            return total_damage - max_damage + 1
        else:
            return total_damage - armor + 1
