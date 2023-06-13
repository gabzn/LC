https://leetcode.com/problems/minimum-cost-to-connect-sticks/
  
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0
    
        cost = 0
        heapify(sticks)
    
        while sticks:
            # This ensures that we have at least 2 sticks
            if len(sticks) == 1:
                break
                
            new_stick = heappop(sticks) + heappop(sticks)
            heappush(sticks, new_stick)
            cost += new_stick
               
        return cost  
