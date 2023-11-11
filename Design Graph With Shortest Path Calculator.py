https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = [[] for _ in range(n)]
        for u, v, c in edges:
            self.graph[u].append((v, c))
        
    def addEdge(self, edge: List[int]) -> None:
        u, v, c = edge
        self.graph[u].append((v, c))

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        cost_to_reach_node = [math.inf for _ in range(self.n)]
        cost_to_reach_node[node1] = 0
        
        while heap:
            c, node = heappop(heap)
            if node == node2:
                return c
            
            for neighbour, n_cost in self.graph[node]:        
                new_cost = n_cost + c
                if new_cost < cost_to_reach_node[neighbour]:
                    cost_to_reach_node[neighbour] = new_cost
                    heappush(heap, (n_cost + c, neighbour))
        
        return -1
