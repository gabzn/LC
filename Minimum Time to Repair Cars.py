https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        r * (n ^ 2) = x
             n ^ 2  = x / r
                 n  = sqrt(x / r)
        """
        def can_fix_cars_in_x_minutes(x):
            cars_fixed = 0
            
            for r in ranks:
                # sqrt(x / r) = # of cars the current mechanic should fix
                cars_fixed += int(sqrt(x // r))
                
            return cars_fixed >= cars
                
        left = 0
        right = 10 ** 15
        
        while left + 1 != right:
            mid = (left + right) // 2
            
            if can_fix_cars_in_x_minutes(mid):
                right = mid
            else:
                left = mid
            
        return right
