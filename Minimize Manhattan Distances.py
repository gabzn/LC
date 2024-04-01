https://leetcode.com/problems/minimize-manhattan-distances/
https://www.geeksforgeeks.org/maximum-manhattan-distance-between-a-distinct-pair-from-n-coordinates/
https://www.youtube.com/watch?v=eLutTwfLQiE&t=1051s

from sortedcontainers import SortedList

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        new_x = SortedList()
        new_y = SortedList()
        
        for x, y in points:
            new_x.add(x + y)
            new_y.add(y - x)
        
        res = inf
        
        for x, y in points:
            new_x.remove(x + y)
            new_y.remove(y - x)
            
            res = min(res, max(new_x[-1] - new_x[0], new_y[-1] - new_y[0]))
            
            new_x.add(x + y)
            new_y.add(y - x)
        
        return res
