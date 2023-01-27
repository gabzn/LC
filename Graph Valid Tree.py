https://leetcode.com/problems/graph-valid-tree/

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(x):
            if x == root[x]:
                return x
            
            root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            
            if root_x == root_y:
                return False
            
            if rank[root_x] > rank[root_y]:
                root[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                root[root_x] = root_y
            else:
                root[root_y] = root_x
                rank[root_x] += 1
            
            return True
        
        if len(edges) != n - 1: 
            return False

        root = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        
        for a, b in edges:
            if not union(a, b):
                return False
        
        return True                 
---------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= len(edges):
            return False
        
        graph = self.make_graph(edges)
        visited_nodes = set()
        queue = deque()
        queue.append((0, 0))
        
        while queue:
            parent, node = queue.popleft()
            visited_nodes.add(node)
            
            # To avoid cycle, I need to know who my parent node is.
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                
                if neighbour in visited_nodes:
                    return False
                
                queue.append((node, neighbour))    
        
        return len(visited_nodes) == n
    
    def make_graph(self, edges):
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        return graph
-------------------------------------------------------------------------------------------------------------------------------------------------------
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
