https://leetcode.com/problems/number-of-operations-to-make-network-connected/

class Solution:
    def build_graph(self, connections):
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        return graph
      
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        graph = self.build_graph(connections)
        visited_nodes = set()
        connected_computers = 0
        
        for node in range(n):
            if node not in visited_nodes:
                connected_computers += 1

                stack = [node]
                while stack:
                    computer = stack.pop()
                    
                    if computer in visited_nodes:
                        continue
                    visited_nodes.add(computer)
                    
                    if computer not in graph:
                        break
                    for neighbour in graph[computer]:
                        stack.append(neighbour)
        
        return connected_computers - 1
---------------------------------------------------------------------------------------------
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False
            
            if rank[root_x] == rank[root_y]:
                root[root_y] = root_x
                rank[root_x] += 1
            elif rank[root_x] > rank[root_y]:
                root[root_y] = root_x
            else:
                root[root_x] = root_y
            return True
        
    
        if len(connections) < n - 1:
            return -1
        """
        The idea is really just to count how many computers are left unconnected.
        We know for sure that some of the connections are redundant meaning two computers are already connected directly or indirectly and there's an extra connection between them. 
        If we encounter a redundant connection, we don't decrement the number of components because we've already done that.
        The reason we are returning n - 1 is because there was an extra edge.
        """        
        root = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        
        for x, y in connections:
            if union(x, y):
                n -= 1

        return n - 1
