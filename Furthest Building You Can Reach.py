https://leetcode.com/problems/furthest-building-you-can-reach/
  
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        LEN = len(heights)
        ladder_heap = []
        
        for current_building, current_building_height in enumerate(heights):
            if current_building == LEN - 1:
                return current_building
            
            next_building_height = heights[current_building + 1]
            if current_building_height >= next_building_height:
                continue
                            
            """
            The next building is higher, use all the ladders first
            
            If in the future we see other higher buildings,
            we can decide if we want to recycle any of the previously used ladders
                If the difference is higher than previously smallest difference
                    We want to recycle the ladder and use it right now and replace it with bricks
                If the difference is smaller than previously smallest difference
                    We don't recycle the ladder. Instead, we use bricks
            
                Every time we use bricks, we check if we have more bricks. 
                If no more bricks, return the current building.
            """
            height_difference = next_building_height - current_building_height
            if ladders:
                heappush(ladder_heap, height_difference)
                ladders -=1
            else:
                if ladder_heap and height_difference > ladder_heap[0]:
                    bricks -= heappop(ladder_heap)
                    heappush(ladder_heap, height_difference)
                else:
                    bricks -= height_difference
                
                if bricks < 0:
                    return current_building     
