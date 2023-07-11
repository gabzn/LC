https://leetcode.com/problems/connecting-cities-with-minimum-cost/

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x, root_y = map(find, [x, y])
            if root_x == root_y:
                return False
            root[root_y] = root_x
            return True
        
        root = [_ for _ in range(n + 1)]
        min_cost, edges_used = 0, 0
      
        connections.sort(key=lambda conn: conn[2])
        for x, y, cost in connections:
            if union(x, y):
                min_cost += cost
                edges_used += 1
                if edges_used == n - 1:
                    return min_cost
    
        return -1
