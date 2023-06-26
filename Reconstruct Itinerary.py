https://leetcode.com/problems/reconstruct-itinerary/

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:        
        tickets.sort()
        graph = self.make_graph(tickets)
        res = []
        
        # Topological ordering
        def postorder_traversal(airport):
            while graph[airport]:
                postorder_traversal(graph[airport].popleft())

            res.append(airport)
                
        postorder_traversal('JFK')
        return reversed(res)
    
    def make_graph(self, tickets):
        graph = defaultdict(deque)
        for departure, arrival in tickets:
            graph[departure].append(arrival)
        return graph
