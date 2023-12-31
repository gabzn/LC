https://leetcode.com/problems/maximum-spending-after-buying-items/

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        TOTAL_DAYS = len(values) * len(values[0])
        
        res = 0
        
        for day in range(1, TOTAL_DAYS + 1):
            store_idx = 0
            min_cost = math.inf
            
            for idx, products in enumerate(values):
                if products and products[-1] < min_cost:
                    min_cost = products[-1]
                    store_idx = idx
                    
            res += (min_cost * day)
            values[store_idx].pop()
        
        return res
