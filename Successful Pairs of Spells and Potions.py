https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def find_leftmost_potion(spell):
            l, r = -1, P
            
            while l + 1 != r:
                m = (l + r) // 2
                potion = potions[m]
                
                if spell * potion >= success:
                    r = m
                else:
                    l = m
            
            return r
        
        S, P = len(spells), len(potions)
    
        potions.sort()
        res = []
        
        for spell in spells:
            res.append(P - find_leftmost_potion(spell))
            
        return res
