https://leetcode.com/problems/optimize-water-distribution-in-a-village/

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        def union(x, y):
            root_x, root_y = map(find, [x, y])
            if root_x == root_y:
                return False
            root[root_y] = root_x
            return True
        
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        
        root = [index for index in range(n + 1)]
        min_cost = 0
        
        for index in range(n):
            house = index + 1
            cost_to_build_well_at_house = wells[index]
            pipes.append([house, 0, cost_to_build_well_at_house])
        
        pipes.sort(key=lambda pipe: pipe[2])
        for house1, house2, cost in pipes:
            if union(house1, house2):
                min_cost += cost
                
        return min_cost
