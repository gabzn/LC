https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:        
        end_of_each_car = {}
        res = 0
        
        # Find out where each car ends
        for idx, g in enumerate(garbage):
            res += len(g)
            
            for t in g:
                end_of_each_car[t] = idx
        
        for _, idx in end_of_each_car.items():
            if idx != 0:
                res += sum(travel[: idx])
        
        return res
