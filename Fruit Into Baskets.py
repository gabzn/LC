https://leetcode.com/problems/fruit-into-baskets/
  
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = collections.defaultdict(int)
        l, r, current_fruits, total_fruits = 0, 0, 0, 0
        
        while r < len(fruits):
            current_f_type = fruits[r]
            counts[current_f_type] += 1
            current_fruits += 1
            
            while len(counts) > 2:
                previous_f_type = fruits[l]
                counts[previous_f_type] -= 1
                if not counts[previous_f_type]:
                    del counts[previous_f_type]
                
                current_fruits -= 1
                l += 1
                
            total_fruits = max(total_fruits, current_fruits)
            r += 1
        
        return total_fruits
