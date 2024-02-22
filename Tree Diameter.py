https://leetcode.com/problems/tree-diameter/

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        def dfs(node, parent):
            distances = []
            
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                
                distances.append(1 + dfs(neighbour, node))
            
            if not distances:
                return 0
            
            distances.sort()    
            res[0] = max(res[0], distances[-1] + (distances[-2] if len(distances) >= 2 else 0))
            
            return distances[-1]
            
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        res = [0]
        dfs(0, -1)
        return res[0]
