https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def find(x):
            if x == root[x]:
                return x
            
            x = find(root[x])
            return x
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    root[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    root[root_x] = root_y
                else:
                    root[root_y] = root_x
                    rank[root_x] += 1
            
        root = [i for i in range(n + 1)]        
        rank = [1 for i in range(n + 1)]
        
        for x, y in edges:
            union(x, y)
        
        return find(source) == find(destination)    
----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True
        
        graph = self.build_graph(edges)
        if source not in graph:
            return False
        
        visited = set()
        stack = [source]
        while stack:
            vertex = stack.pop()
            if vertex == destination:
                return True
            
            visited.add(vertex)
            
            for v in graph[vertex]:
                if v not in visited:
                    stack.append(v)
        
        return False
    
    def build_graph(self, edges):
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        return graph  
------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True
        
        graph = self.build_graph(edges)
        if source not in graph:
            return False
        
        return self.dfs(graph, source, destination, set())
    
    def build_graph(self, edges):
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        return graph
    
    def dfs(self, graph, source, destination, visited):
        if source == destination:
            return True
        
        visited.add(source)
        for v in graph[source]:
            if v not in visited and self.dfs(graph, v, destination, visited):
                return True
        
        return False
