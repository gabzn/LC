https://leetcode.com/problems/bus-routes/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:    
        stop_to_buses = defaultdict(list)
        for idx, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(idx)
        
        visited_buses = set()
        visited_stops = set()
        visited_stops.add(source)
        
        queue = deque([(source, 0)])
        while queue:
            stop, buses_taken = queue.popleft()
            if stop == target:
                return buses_taken
            
            for bus in stop_to_buses[stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                
                for next_stop in routes[bus]:
                    if next_stop in visited_stops:
                        continue
                    visited_stops.add(next_stop)
                    
                    queue.append((next_stop, buses_taken + 1))
                    
        return -1
