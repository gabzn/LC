https://leetcode.com/problems/maximum-number-of-alloys/

class Solution:
    def maxNumberOfAlloys(self, n: int, machines: int, budget: int, mats_needed_for_each_machine: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def max_alloys_made_by_machine_i(i, budget):
            left, right = -1, 10**10
            
            while left + 1 != right:
                mid = (left + right) // 2
                
                if can_make_x_alloys(mid, i, budget):
                    left = mid
                else:
                    right = mid
            
            return left
        
        def can_make_x_alloys(x, i, budget):
            materials = mats_needed_for_each_machine[i]
            
            mats_needed_to_make_x_alloys = []
            for mat in materials:
                mats_needed_to_make_x_alloys.append(mat * x)
            
            for i in range(len(mats_needed_to_make_x_alloys)):
                own = stock[i]
                need = mats_needed_to_make_x_alloys[i]
                
                # We have enough of the current materials to make x alloys
                if own >= need:
                    continue
                
                # We don't have enough. We need to buy
                cost_per_each = cost[i]
                to_buy = need - own
                budget -= (cost_per_each * to_buy)
    
            return budget >= 0
                
        res = 0
        
        for machine in range(machines):
            res = max(max_alloys_made_by_machine_i(machine, budget), res)
        
        return res
