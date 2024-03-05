https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], speed: int) -> List[int]:                         
        def dfs(node, parent, w):
            valid_nodes = (w % speed == 0)
            
            for neighbour, weight in graph[node]:
                if neighbour == parent:
                    continue            
                valid_nodes += dfs(neighbour, node, w + weight)
        
            return valid_nodes
        
        N = len(edges) + 1
        
        graph = [[] for _ in range(N)]
        for a, b, w in edges:
            graph[a].append((b, w))
            graph[b].append((a, w))
        
        count = [0 for _ in range(N)]
        
        for node in range(N):
            valid_pairs = 0
            num_valid_nodes_on_other_sides = 0
            
            for neighbour, weight in graph[node]:
                num_valid_nodes_on_one_side = dfs(neighbour, node, weight)
                
                valid_pairs += num_valid_nodes_on_other_sides * num_valid_nodes_on_one_side
                num_valid_nodes_on_other_sides += num_valid_nodes_on_one_side
            
            count[node] = valid_pairs    
        return count
