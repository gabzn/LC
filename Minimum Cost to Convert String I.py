https://leetcode.com/problems/minimum-cost-to-convert-string-i/

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def index(char):
            return ord(char) - ord('a')
        
        # Dijkstra compute the min distance from "s" to all others 
        def dijkstra(s):
            heap = [(0, s)]
            
            while heap:
                cur_cost, x = heappop(heap)
                
                for y, next_cost in graph[x]:
                    new_cost = cur_cost + next_cost
                    
                    if new_cost <= distances[index(s)][index(y)]:
                        distances[index(s)][index(y)] = new_cost
                        heappush(heap, (new_cost, y))
        
        distances = [[math.inf if i != j else 0 for j in range(26)] for i in range(26)]
        graph = defaultdict(list)
        
        # Create the graph and fill in values for distances
        for s, t, c in zip(original, changed, cost):
            s_i, t_i = map(index, [s, t])
            distances[s_i][t_i] = min(distances[s_i][t_i], c)
            
            graph[s].append((t, c))
        
        # Use dijkstra on each letter in the graph to find the min distance from this letter to all others
        for i in range(26):
            s = chr(i + ord('a'))
            if s not in graph:
                continue
                            
            dijkstra(s)
        
        res = 0
        
        for s, t in zip(source, target):
            s_i, t_i = map(index, [s, t])
            distance = distances[s_i][t_i]
            
            if distance == math.inf:
                return -1
            res += distance
              
        return res
