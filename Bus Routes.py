https://leetcode.com/problems/bus-routes/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_buses = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].add(i)
        
        visited_buses = set()
        visited_stops = set([source])
        queue = deque([(source, 0)])
        while queue:
            stop, total_buses = queue.popleft()
            if stop == target:
                return total_buses
            
            for bus in stop_to_buses[stop]:
                # We don't add the first bus to visited because 
                # it may contain other stops we can go to from this bus
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                
                for next_stop in routes[bus]:
                    if next_stop in visited_stops:
                        continue
                    
                    visited_stops.add(next_stop)
                    queue.append((next_stop, total_buses + 1))

        return -1
