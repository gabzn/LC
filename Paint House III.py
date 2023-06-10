https://leetcode.com/problems/paint-house-iii/

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # n is the number of colors ranging from 1 - n
        # m is the length of houses and cost
        # target is the number of neighbourhoods we want    
        def dp(i, prev_color, hoods, memo):
            if i == m:
                return 0 if hoods == target else math.inf
            if (i, prev_color, hoods) in memo:
                return memo[(i, prev_color, hoods)]
            
            memo[(i, prev_color, hoods)] = math.inf
            
            """
            There are only two scenarios at each step.
                1. The current house needs to be painted.
                2. The current house doesn't need to be painted.
            """
            if houses[i] == 0:
                """
                If the current house needs painting, we go through the cost at painting this house.
                    If the current color is the same as the previous house, we don't increment the # of hoods.
                    If the current color is not the same as the previous house, we increment the # of hoods.
                """
                for idx, c in enumerate(cost[i]):
                    same_color = different_color = math.inf
                    if idx + 1 == prev_color:
                        same_color = c + dp(i + 1, prev_color, hoods, memo)
                    else:
                        different_color = c + dp(i + 1, idx + 1, hoods + 1, memo)
                    
                    memo[(i, prev_color, hoods)] = min(memo[(i, prev_color, hoods)], same_color, different_color)    
            else:
                """
                If the current house doesn't need painting, we check if the current house has the same color as the previous house.
                    If it does, we don't increment the # of hoods.
                    If it doesn't, we increment the # of hoods.
                """
                if houses[i] == prev_color:
                    memo[(i, prev_color, hoods)] = dp(i + 1, houses[i], hoods, memo)
                else:
                    memo[(i, prev_color, hoods)] = dp(i + 1, houses[i], hoods + 1, memo)

            return memo[(i, prev_color, hoods)]
        
        min_cost = dp(0, 0, 0, {}) 
        return min_cost if min_cost != math.inf else -1  
