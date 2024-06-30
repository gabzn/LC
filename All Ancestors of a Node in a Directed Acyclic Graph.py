https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        indegrees = [0 for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            indegrees[b] += 1
        
        res = [set() for _ in range(n)]
        queue = deque()
        for i, degree in enumerate(indegrees):
            if degree == 0:
                queue.append(i)
        
        while queue:
            parent = queue.popleft()
            
            for child in graph[parent]:
                if res[parent]:
                    res[child] = res[child].union(res[parent])
                res[child].add(parent)
                
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)
                    
        return [sorted(list(s)) for s in res]
