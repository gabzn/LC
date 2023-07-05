https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for departure, arrival, price in flights:
            adj_list[departure].append((arrival, price))
        
        cheapest_to_node = [math.inf for _ in range(n)]
        
        # Dijkstra solution uses the number of stops as its priority instead of the cost
        heap = [(0, 0, src)]
        while heap:
            stops, cost, node = heappop(heap)
            
            # Skip the current iteration if any of the two conditions is met:
            #   If the current node is dst and the number of stops is still valid
            #   If the current node is not dst but the number of stops cannot support further stops
            if (node == dst and stops <= k + 1) or (stops >= k + 1):
                continue
                            
            for neighbour, price in adj_list[node]:
                cost_to_reach_neighbour = price + cost
                if cost_to_reach_neighbour >= cheapest_to_node[neighbour]:
                    continue
                
                cheapest_to_node[neighbour] = cost_to_reach_neighbour
                heappush(heap, (stops + 1, cost_to_reach_neighbour, neighbour))
                
        return cheapest_to_node[dst] if cheapest_to_node[dst] != math.inf else -1
--------------------------------------------------------------------------------------
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for departure, arrival, price in flights:
            adj_list[departure].append((arrival, price))
        
        cheapest_to_node = [math.inf for _ in range(n)]
        
        queue = deque([(src, 0, 0)])
        while queue:
            node, cost, stops = queue.popleft()
            
            # Skip the current iteration if any of the two conditions is met:
            #   If the current node is dst and the number of stops is still valid
            #   If the current node is not dst but the number of stops cannot support further stops
            if (node == dst and stops <= k + 1) or (stops >= k + 1):
                continue            
            
            for neighbour, price in adj_list[node]:
                cost_to_reach_neighbour = price + cost
                if cost_to_reach_neighbour >= cheapest_to_node[neighbour]:
                    continue

                cheapest_to_node[neighbour] = cost_to_reach_neighbour
                queue.append((neighbour, cost_to_reach_neighbour, stops + 1))
                                 
        return cheapest_to_node[dst] if cheapest_to_node[dst] != math.inf else -1
