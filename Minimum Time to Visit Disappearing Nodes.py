https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:    
        graph = [[] for _ in range(n)]
        for a, b, v in edges:
            graph[a].append((b, v))
            graph[b].append((a, v))
        
        time_to_reach = [math.inf for _ in range(n)]
        time_to_reach[0] = 0
        
        heap = [(0, 0)]
        while heap:
            t, node = heappop(heap)
            if t > time_to_reach[node]:
                continue
            
            for neighbour, time in graph[node]:
                new_time = time + t
                
                if new_time <= time_to_reach[neighbour] and new_time < disappear[neighbour]:
                    time_to_reach[neighbour] = new_time
                    heappush(heap, (new_time, neighbour))
       
        return [t if t != math.inf else -1 for t in time_to_reach]
