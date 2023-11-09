https://leetcode.com/problems/squirrel-simulation/

class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def compute_distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        distance = 0
        saving = math.inf
        
        # Assume the squirrel is at the tree initially
        for nx, ny in nuts:
            nut_to_tree = (compute_distance([nx, ny], tree))
            round_trip = 2 * nut_to_tree
            
            distance += round_trip
            
            # If the squirrel is at some random location initially
            saving = min(saving, compute_distance([nx, ny], squirrel) - nut_to_tree)
                    
        return distance + saving
