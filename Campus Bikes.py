https://leetcode.com/problems/campus-bikes/

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n, m = map(len, [workers, bikes])
        res = [-1 for _ in range(n)]
        
        workers_distances_to_bikes = []
        for i, [wx, wy] in enumerate(workers):
            for j, [bx, by] in enumerate(bikes):
                distance = abs(wx - bx) + abs(wy - by)
                workers_distances_to_bikes.append((distance, i, j))
        
        workers_distances_to_bikes.sort()
        is_bike_available = [True for _ in range(m)]
        total_assignments = 0
        
        for _, worker, bike in workers_distances_to_bikes:
            if res[worker] == -1 and is_bike_available[bike]:
                res[worker] = bike
                is_bike_available[bike] = False
                total_assignments += 1
            
            if total_assignments == n:
                break
            
        return res
