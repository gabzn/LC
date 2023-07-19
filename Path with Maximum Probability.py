https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], probs: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for index, (a, b) in enumerate(edges):
            graph[a].append((b, probs[index]))
            graph[b].append((a, probs[index]))
                
        max_probability_to_each_node = [0.0 for _ in range(n)]
        max_probability_to_each_node[start] = 1.0
        
        heap = [(-1.0, start)]
        while heap:
            prob, node = heappop(heap)
            
            for neighbour, prob_to_neighbour in graph[node]:
                culmulative_prob = -prob * prob_to_neighbour
                
                if culmulative_prob > max_probability_to_each_node[neighbour]:
                    max_probability_to_each_node[neighbour] = culmulative_prob
                    heappush(heap, (-culmulative_prob, neighbour))
                    
        return max_probability_to_each_node[end]
