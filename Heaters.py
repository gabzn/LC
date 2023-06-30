https://leetcode.com/problems/heaters/
https://www.youtube.com/watch?v=K-Jz5eB1NIw&t=14s

# https://www.youtube.com/watch?v=K-Jz5eB1NIw&t=14s
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()    # n logn
        res = 0
        
        # We want to find the shortest radius for each house
        # Then we want to pick the max from these shortest radii.
        # m logn
        for house in houses:   
            res = max(res, self.find_shortest_radius(heaters, house))  
        
        # (m + n) logn
        return res

    # bisect left
    def find_shortest_radius(self, heaters, house):
        l, r = -1, len(heaters)
        shortest_radius = math.inf
        
        while l + 1 != r:
            m = (l + r) // 2
            shortest_radius = min(shortest_radius, abs(house - heaters[m]))
            
            if heaters[m] < house:
                l = m
            else:
                r = m
        
        return shortest_radius
------------------------------------------------------------------------------------
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Sort the houses and heaters
        houses.sort()
        heaters.sort()

        res = 0

        # For each house, find the closest heater to the left and the right
        for house in houses:
            left = bisect.bisect_right(heaters, house) - 1
            right = bisect.bisect_left(heaters, house)

            # If the house is to the left of all heaters, use the closest heater to the left
            if left < 0:
                res = max(res, heaters[0] - house)
            # If the house is to the right of all heaters, use the closest heater to the right
            elif right == len(heaters):
                res = max(res, house - heaters[-1])
            # If the house is between two heaters, use the closer of the two
            else:
                res = max(res, min(house - heaters[left], heaters[right] - house))

        return res
