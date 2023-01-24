class UnionFind:

    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
    
    # Union combines x y to the same set 
    def union(self, x, y) -> None:
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    # Find returns the root of x
    def find(self, x):
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]
