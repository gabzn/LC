class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def union(x, y):
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
        
        def find(x):
            if x == root[x]:
                return x
            
            root[x] = find(root[x])
            return root[x]
        
        root = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        components = [n]
        
        for a, b in edges:
            union(a, b)
        
        return components[0]
