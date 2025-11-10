https://leetcode.com/problems/fruit-into-baskets/
  
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = defaultdict(int)
        res = 0
        left = 0

        for right, fruit in enumerate(fruits):
            counter[fruit] += 1

            while len(counter) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                left += 1
            
            res = max(right - left + 1, res)
        
        return res
