https://leetcode.com/problems/redundant-connection/
  
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            
            if root_x == root_y:
                return True
            
            root[root_y] = root_x
            return False
        
        N = len(edges)
        root = [i for i in range(N + 1)]
        
        for a, b in edges:
            if union(a, b):
                return [a, b]
