https://leetcode.com/problems/heaters/

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
