https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return
        
            root[root_y] = root_x
            provinces[0] -= 1
        
        N = len(isConnected)
        provinces = [N]
        root = [i for i in range(N)]
        
        for i, cities in enumerate(isConnected):
            for j, city in enumerate(cities):
                if i == j or city == 0:
                    continue
                union(i, j)
                
        return provinces[0]
-------------------------------------------------------------------------------------
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return
        
            provinces[0] -= 1
        
            if rank[root_x] > rank[root_y]:
                root[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                root[root_x] = root_y
            else:
                root[root_y] = root_x
                rank[root_x] += 1
        
        N = len(isConnected)
        provinces = [N]
        root = [i for i in range(N)]
        rank = [1 for _ in range(N)]
        
        for i, cities in enumerate(isConnected):
            for j, city in enumerate(cities):
                if i == j or city == 0:
                    continue
                union(i, j)
                
        return provinces[0]
