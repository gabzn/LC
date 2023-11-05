https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0 for _ in range(n)]
        for a, b in edges:
            indegree[b] += 1
        
        start = []
        for node, degree in enumerate(indegree):
            if degree > 0:
                continue

            start.append(node)
            if len(start) > 1:
                return -1
                
        return start[0]
