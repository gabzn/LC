https://leetcode.com/problems/buildings-with-an-ocean-view/
  
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        max_height = -math.inf
        
        for index in range(len(heights)-1, -1, -1):
            if heights[index] > max_height:
                res.append(index)
                max_height = heights[index]
        
        res.reverse()
        return res
