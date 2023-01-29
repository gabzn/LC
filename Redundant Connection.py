https://leetcode.com/problems/redundant-connection/
  
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            
            # If both nodes happen to have the same parent, that means they are already connected 
            # through the parent. Adding an edge between them causes a cycle.
            if root_x == root_y:
                return True
            
            if rank[root_x] == rank[root_y]:
                root[root_y] = root_x
                rank[root_x] += 1
            elif rank[root_x] > rank[root_y]:
                root[root_y] = root_x
            else:
                root[root_x] = root_y
            
            return False
        
        N = len(edges)
        root = [i for i in range(N + 1)]
        rank = [1 for _ in range(N + 1)]
        res = []
        
        for edge in edges:
            x, y = edge
            if union(x, y):
                res = edge
        
        return res
