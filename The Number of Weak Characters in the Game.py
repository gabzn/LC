https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
  
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """
        Sort properties by attack in ascending order and defense in descending order.
        
        By doing this, we can know for sure if current defense > max_defense,
        their attacks must be equal.
            We update the max_defense if their attacks are equal.
        
        If the current defense < max_defense, the current character is a weak character.        
        """
        properties.sort(key=lambda p: (p[0], -p[1]))
        max_defense = properties[-1][1]
        res = 0
        
        for index in range(len(properties)-1, -1, -1):
            current_defense = properties[index][1]
            
            if current_defense < max_defense:
                res += 1
            else:
                max_defense = current_defense
            
        return res
