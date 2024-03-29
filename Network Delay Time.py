https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.make_graph(times)
        
        # signal_received_at_time[x] stores what time node x receives any signal
        # Initially set to math.inf to indicate that no signal was received
        signal_received_at_time = [math.inf for _ in range(n + 1)]
        signal_received_at_time[k] = 0
        
        queue = [(k, 0)]
        while queue:
            node, cur_time = heappop(queue)
            
            # Add neighbour_node to queue only if traversing this path takes
            # less time than the value at signal_received_at_time[neighbour_node]
            for neighbour_node, time in graph[node]:
                new_time = cur_time + time
                
                if new_time < signal_received_at_time[neighbour_node]:
                    signal_received_at_time[neighbour_node] = new_time
                    heappush(queue, (neighbour_node, new_time))
        
        max_time = max(signal_received_at_time[1:])
        return max_time if max_time != math.inf else -1
        
    def make_graph(self, times):
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))
        return graph
-----------------------------------------------------------------------------------
class Solution:
        
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Sort the times based on the time to send signal
        times.sort(key=lambda time: time[2])
        graph = self.make_graph(times)

        # Create a list to show when the nodes receive the signal
        # Initially, they are math.inf to indicate they haven't received any signal
        # signal_received_at_time[0] = -1 is to invalidate the first slot because nodes are from 1 to n.
        signal_received_at_time = [math.inf for _ in range(n + 1)]
        signal_received_at_time[0] = -1
        
        def dfs(node, cur_time):
            # If cur_time is >= signalReceivedAt[currNode], return
            if cur_time >= signal_received_at_time[node]:
                return
            
            # Set signal_received_at_time[node] equal to cur_time which is the new shortest time required to reach node
            signal_received_at_time[node] = cur_time
            
            # Perform DFS on the adjacent nodes using the updated timestamp.
            for target, time in graph[node]:
                dfs(target, time + cur_time)
        
        dfs(k, 0)
        max_time = max(signal_received_at_time)
        return max_time if max_time != math.inf else -1     
    
    def make_graph(self, times):
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))
        return graph      
