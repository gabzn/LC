https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        
        # Kahn's Algorithm - Topo sort
        indegree = [0] * N
        for to in edges:
            indegree[to] += (to != -1)
                
        # all the nodes not in the cycle would be visited and 
        # only the nodes in the cycle would be not visited 
        queue = deque([node for node, degree in enumerate(indegree) if degree == 0])        
        while queue:
            node = queue.popleft()
            
            neighbour = edges[node]
            if neighbour == -1:
                continue
            
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
        
        # If there are nodes that still have indegree > 0, there are cycles
        # DFS on nodes that have indegree > 0, and find the max length
        res = -1
        visited_nodes = set()
        
        for node, degree in enumerate(indegree):
            if degree > 0 and node not in visited_nodes:
                
                cycle_length = 1                
                visited_nodes.add(node)
                stack = [node]
                
                while stack:
                    node = stack.pop()
                    
                    neighbour = edges[node]
                    if neighbour not in visited_nodes:
                        visited_nodes.add(neighbour)
                        stack.append(neighbour)
                        cycle_length += 1
                
                res = max(res, cycle_length)
        
        return res
