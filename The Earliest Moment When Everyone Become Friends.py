https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/
  
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x, y, timestamp):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    root[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    root[root_x] = root_y                
                else:
                    root[root_y] = root_x
                    rank[root_x] += 1
                
                components[0] -= 1
                if components[0] == 1:
                    time[0] = timestamp
                    return True
                return False
        
        logs.sort(key=lambda log: log[0])
        
        root = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        
        # If the number of components can be reduced to 1, that means they can all be friends. Thus, a solution exists.
        time, components = [math.inf], [n]
        
        for t, a, b in logs:
            if union(a, b, t):
                return time[0]
        
        return -1
