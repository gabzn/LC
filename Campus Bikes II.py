https://leetcode.com/problems/campus-bikes-ii/

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:        
        def compute_distance(wx, wy, bx, by):
            return abs(wx - bx) + abs(wy - by)
        
        @cache
        def dp(worker_idx, bike_mask):
            if worker_idx == TOTAL_WORKERS:
                return 0
            
            res = math.inf
            
            for bike_idx in range(TOTAL_BIKES):
                if bike_mask & (1 << bike_idx):
                    distance = compute_distance(*workers[worker_idx], *bikes[bike_idx])
                    res = min(res, distance + dp(worker_idx + 1, bike_mask ^ (1 << bike_idx)))
            
            return res
            
        TOTAL_WORKERS, TOTAL_BIKES = map(len, [workers, bikes])        
        return dp(0, (1 << TOTAL_BIKES) - 1)
