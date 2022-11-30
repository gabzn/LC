https://leetcode.com/problems/evaluate-division/
  
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
  
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.build_graph(equations, values)
        res = []
        
        for num, den in queries:
            # #s not in the graph
            if num not in graph or den not in graph:
                res.append(-1.0)
                
            # a / a
            elif num == den:
                res.append(1.0)
            
            # evaluate num / den
            else:
                res.append(self.bfs(graph, num, den, -1.0))
            
        return res
    
    def bfs(self, graph, num, den, ans):
        visited = set()
        queue = deque()
        queue.append((num, 1.0))
    
        while queue:
            number, val = queue.popleft()
                
            if number == den:
                ans = val
                break
                
            if number in visited:
                continue
            visited.add(number)
                
            for neighbour in graph[number]:
                queue.append((neighbour[0], val*neighbour[1]))
        
        return ans
        
    def build_graph(self, equations, values):
        graph = defaultdict(list)
        
        for ind ,[num, den] in enumerate(equations):
            graph[num].append((den, values[ind]))            
            graph[den].append((num, 1 / values[ind]))
            
        return graph
