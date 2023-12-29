https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        distances = [[math.inf if i != j else 0 for j in range(n)] for i in range(n)]
        
        # Initialize distances with the given weights
        for a, b, weight in edges:
            distances[a][b] = weight
            distances[b][a] = weight
        
        # Perform Floyd-Warsall to get the shortest distances for every pair of nodes
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
        
        res = None
        
        for i in range(n):
            reachable_count = 0
            
            for j in range(n):    
                if i != j and distances[i][j] <= threshold:
                    reachable_count += 1
                        
            if res == None:
                res = (i, reachable_count)
            else:
                _, prev_count = res
                if reachable_count <= prev_count:
                    res = (i, reachable_count)
        
        return res[0]
---------------------------------------------------------------------------------------------------------------
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        def dijkstra(source):
            heap = [(0, source)]
            
            while heap:
                cur_cost, node = heappop(heap)
                
                for neighbour, next_cost in graph[node]:                      
                    new_cost = cur_cost + next_cost
                    
                    if new_cost <= distances[source][neighbour]:
                        distances[source][neighbour] = new_cost
                        heappush(heap, (new_cost, neighbour))
                        
        distances = [[math.inf if i != j else 0 for j in range(n)] for i in range(n)]                        
        graph = defaultdict(list)
        
        for a, b, weight in edges:
            graph[a].append((b, weight))
            graph[b].append((a, weight))
            
            distances[a][b] = weight
            distances[b][a] = weight
        
        # Perform dijkstra on every single node to find the shortest distance from node to others
        for node in range(n):
            dijkstra(node)
        
        res = None
                
        for i in range(n):
            reachable_count = 0
            cities = []
            
            for j in range(n):    
                if i != j and distances[i][j] <= threshold:
                    reachable_count += 1
                    cities.append(j)
                    
            if res == None:
                res = (i, reachable_count)
            else:
                _, prev_count = res
                if reachable_count <= prev_count:
                    res = (i, reachable_count)
                                                    
        return res[0]
