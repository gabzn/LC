https://leetcode.com/problems/graph-valid-tree/
  
You have a graph of n nodes labeled from 0 to n - 1. 
You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.


from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = self.convert_edges_to_graph(edges)
        
        # Always start dfs on the 0 node, the parent of the 0 node doesn't exist so we can set its parent to -1.
        stack = [(0, -1)]
        visited_nodes = set()
        
        return self.dfs(graph, stack, visited_nodes) and len(visited_nodes) == n
    
    """
        We can use dfs to detect if there's any cycles in the tree.
        Return True if there's no cycles.
        Return False if there's a cycle.
    """
    def dfs(self, graph, stack, visited_nodes):
        while stack:
            cur_node, parent_node = stack.pop()
            visited_nodes.add(cur_node)
            
            for neighbour in graph[cur_node]:    
                # If this neighour is the root/parent of the current node, it doesn't count as having a cycle.
                if neighbour == parent_node:
                    continue
                
                # If this neighbour is already been added to the set and it's not the parent, that means there's a cycle.
                if neighbour in visited_nodes:
                    return False
                
                # The neighbour is not a parent and has not been visited yet. Push it to the stack to explore.
                stack.append((neighbour, cur_node))
        
        return True
        
    def convert_edges_to_graph(self, edges):
        graph = defaultdict(list)
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        return graph     
    
"""
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = self.convert_edges_to_graph(edges)
        visited_nodes = set()
                
        return self.dfs(graph, 0, -1, visited_nodes) and len(visited_nodes) == n
            
    def dfs(self, graph, node, parent_node, visited_nodes):
        visited_nodes.add(node)
        
        for neighbour in graph[node]:
            if neighbour == parent_node:
                continue
            
            if neighbour in visited_nodes:
                return False
            
            self.dfs(graph, neighbour, node, visited_nodes)
        
        return True
"""
