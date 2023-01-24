class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:        
        def find(x):
            if x == root[x]:
                return x

            root[x] = find(root[x])
            return root[x]

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
                
                provinces[0] -= 1
        
        N = len(isConnected)
        provinces = [N]

        root = [i for i in range(N + 1)]
        rank = [1] * (N + 1)
        
        for idx, connection in enumerate(isConnected):
            for i, city in enumerate(connection):
                if city == 1:
                    union(idx + 1, i + 1)
        
        # # Count the number of root nodes that are equal to themselves.         
        # res = -1
        # for idx, r in enumerate(root):
        #     if idx == r:
        #         res += 1
        # return res
        
        return provinces[0]
