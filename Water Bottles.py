https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, num_bottles: int, exchange: int) -> int:
        empty_bottles = 0
        
        while num_bottles:
            num_bottles -= 1
            empty_bottles += 1
            
            if empty_bottles % exchange == 0:
                num_bottles += 1
        
        return empty_bottles
