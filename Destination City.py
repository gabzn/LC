https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        out_degree = {}
        
        for a, b in paths:
            if a in paths:
                out_degree[a] += 1
            else:
                out_degree[a] = 1
            
            if b not in out_degree:
                out_degree[b] = 0
        
        for city, degree in out_degree.items():
            if degree == 0:
                return city
