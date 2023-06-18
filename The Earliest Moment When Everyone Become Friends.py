https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/
  
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False
            
            root[root_y] = root_x
            return True
        
        logs.sort(key=lambda log: log[0])
        root = [i for i in range(n)]
        groups = n
                
        for timestamp, x, y in logs:
            if union(x, y):
                groups -= 1
            if groups == 1:
                return timestamp
                
        return -1
