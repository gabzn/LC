https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False
            root[root_y] = root_x
            return True
        
        LEN = len(points)
        min_cost, edges_used = 0, 0
        root = [_ for _ in range(LEN)]
        
        # Construct all the edges
        edges = []
        for current_pt in range(LEN):
            for next_pt in range(current_pt + 1, LEN):
                weight = abs(points[current_pt][0] - points[next_pt][0]) + \
                         abs(points[current_pt][1] - points[next_pt][1])
                edges.append((weight, current_pt, next_pt))
        
        # Sort the edges by weights to achieve min cost
        edges.sort(key=lambda edge: edge[0])
        
        for weight, pt1, pt2 in edges:
            # Make sure the current edge doesn't form a cycle
            # If it doesn't form a cycle, pick this edge and add the cost
            if union(pt1, pt2):
                min_cost += weight
                edges_used += 1
                
                # Kruskal's Algorithm needs only N - 1 edges where N is the number of points
                if edges_used == LEN - 1:
                    break

        return min_cost
