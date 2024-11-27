https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegrees = [0] * n
        for _, b in edges:
            indegrees[b] += 1

        unique_count = 0
        champ = -1
        for i, degree in enumerate(indegrees):
            if degree == 0:
                unique_count += 1
                if unique_count == 2:
                    return -1
                champ = i
        
        return champ
