https://leetcode.com/problems/find-edges-in-shortest-paths/
https://www.youtube.com/watch?v=O7cOWV_SKNg

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for i, (a, b, w) in enumerate(edges):
            graph[a].append((b, w, i))
            graph[b].append((a, w, i))
        
        distances = [inf for _ in range(n)]
        distances[0] = 0
        heap = [(0, 0)]
        while heap:
            dist, node = heappop(heap)
            if dist > distances[node]:
                continue
            
            for neighbour, weight, _ in graph[node]:
                new_dist = dist + weight
                if new_dist < distances[neighbour]:
                    distances[neighbour] = new_dist
                    heappush(heap, (new_dist, neighbour))
        
        res = [False] * len(edges)
        if distances[-1] == inf:
            return res
        
        visited = set([n-1])
        stack = [n-1]
        while stack:
            node = stack.pop()
            
            for neighbour, weight, i in graph[node]:
                if distances[neighbour] + weight == distances[node]:
                    res[i] = True
                    visited.add(neighbour)
                    stack.append(neighbour)
        
        return res
