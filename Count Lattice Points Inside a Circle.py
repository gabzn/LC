https://leetcode.com/problems/count-lattice-points-inside-a-circle/

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        
        for center_x, center_y, radius in circles:
            low_x, high_x = center_x - radius, center_x + radius
            low_y, high_y = center_y - radius, center_y + radius
            
            for x in range(low_x, high_x + 1):
                for y in range(low_y, high_y + 1):
                    delta_x = abs(x - center_x)
                    delta_y = abs(y - center_y)
                    
                    # Distance formula to check if a point is insdie a circle
                    # x^2 + y^2 <= r^2
                    if pow(delta_x, 2) + pow(delta_y, 2) <= pow(radius, 2):
                        points.add((x, y))
            
        return len(points)
