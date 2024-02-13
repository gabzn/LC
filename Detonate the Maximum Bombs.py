https://leetcode.com/problems/detonate-the-maximum-bombs/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(i):
            res = 0
            stack = [i]
            visited = set([i])
            
            while stack:
                node = stack.pop()
                res += 1
                
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        stack.append(neighbour)
            
            return res
       
        LEN = len(bombs)            
        graph = defaultdict(list)

        for i in range(LEN):
            for j in range(LEN):
                if i == j:
                    continue
                
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]
                
                delta_x = xi - xj
                delta_y = yi - yj
                
                # Check if two circles intersect or touch
                if pow(delta_x, 2) + pow(delta_y, 2) <= pow(ri, 2):
                    graph[i].append(j)
                    
        res = 1

        for i in range(LEN):
            res = max(res, dfs(i))
         
        return res
