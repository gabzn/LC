https://leetcode.com/problems/water-bottles-ii/

class Solution:
    def maxBottlesDrunk(self, bottles: int, exchange: int) -> int:
        res = 0
        empty = 0
        
        while bottles:
            res += bottles
            empty += bottles
            bottles = 0
            
            if empty >= exchange:
                bottles += 1
                empty -= exchange
                exchange += 1
                
        return res
