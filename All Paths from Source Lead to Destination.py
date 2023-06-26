https://leetcode.com/problems/all-paths-from-source-lead-to-destination/
https://www.youtube.com/watch?v=hxhX4LSx5XM

class Solution:
    def make_graph(self, edges):
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        return graph
    
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.make_graph(edges)
        if source not in graph:
            return source == destination
        
        memo, visited_nodes = {}, set()
    
        def dfs(node):
            if node in memo:
                return memo[node]
            
            # If there's no more neighbours, return true when the current node is the destination.
            if not graph[node]:
                return node == destination
            
            if node in visited_nodes:
                return False
            visited_nodes.add(node)
            
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
                
            visited_nodes.remove(node)
            memo[node] = True
            return True
                        
        return dfs(source)
