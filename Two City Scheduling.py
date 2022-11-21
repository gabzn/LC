https://leetcode.com/problems/two-city-scheduling/
  
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_cost = 0
        """
        The cost of sending a person to A - The cost of sending a person to B
        tells us how much we can save if we send him to A rather than B
        
        If the difference is negative, that means sending him to A will result in lower cost.
        If the difference is positive, that means sending him to B will result in lower cost.
        10, 100 -> -90
        300, 500 -> -200
        1000, 600 -> 400
        200, 40  -> 160
        
        Sort by the cost differences, we'll know that the first half should be sent to A
        and the other half should be sent to B
        
        300, 500 -> -200    to A
        10, 100 -> -90      to A
        200, 40  -> 160     to B
        1000, 600 -> 400    to B
        """
        costs.sort(key=lambda cost: cost[0] - cost[1])
        
        # The first half should be sent to A
        for i in range(0, len(costs) // 2):
            min_cost += costs[i][0]
        
        # The second half should be sent to B
        for i in range(len(costs) // 2, len(costs)):
            min_cost += costs[i][1]
        
        return min_cost
