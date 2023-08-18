https://leetcode.com/problems/maximal-network-rank/

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = self.make_graph(roads)
        res = 0
        
        for city_one in range(n):
            for city_two in range(city_one):
                city_one_indegree = len(graph[city_one])
                city_two_indegree = len(graph[city_two])
                
                if city_two in graph[city_one]:
                    res = max(res, city_one_indegree + city_two_indegree - 1)
                else:
                    res = max(res, city_one_indegree + city_two_indegree)

        return res              
    
    def make_graph(self, roads):
        graph = defaultdict(set)        
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        return graph
