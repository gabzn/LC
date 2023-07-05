https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for departure, arrival, price in flights:
            adj_list[departure].append((arrival, price))
        
        cheapest_to_node = [math.inf for _ in range(n)]
        
        queue = deque([(src, 0, 0)])
        while queue:
            node, cost, stops = queue.popleft()
                    
            for neighbour, price in adj_list[node]:
                cost_to_reach_neighbour = price + cost
                if cost_to_reach_neighbour >= cheapest_to_node[neighbour]:
                    continue
                
                # If neighbour is dst and the number of stops is less than or equal to k
                if neighbour == dst and stops <= k:
                    cheapest_to_node[neighbour] = cost_to_reach_neighbour
                    queue.append((neighbour, cost_to_reach_neighbour, stops + 1))
                    continue
                    
                # If neighbour is not dst and the number of stops + 1 is still less than or equal to k
                if stops + 1 <= k:
                    cheapest_to_node[neighbour] = cost_to_reach_neighbour
                    queue.append((neighbour, cost_to_reach_neighbour, stops + 1))                    
                
        return cheapest_to_node[dst] if cheapest_to_node[dst] != math.inf else -1
