https://leetcode.com/problems/fruit-into-baskets/
  
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:    
        baskets_of_fruits = collections.defaultdict(int)
        l, cur_count, max_count = 0, 0, 0
        
        for r in range(len(fruits)):            
            baskets_of_fruits[fruits[r]] += 1
            cur_count += 1
            
            while len(baskets_of_fruits) > 2:
                baskets_of_fruits[fruits[l]] -= 1                
                
                if baskets_of_fruits[fruits[l]] == 0:
                    del baskets_of_fruits[fruits[l]]
                
                cur_count -= 1
                l += 1
                
            max_count = max(max_count, cur_count)
        
        return max_count
