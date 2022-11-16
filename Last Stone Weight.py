https://leetcode.com/problems/last-stone-weight/
  
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1     
        
        heapq.heapify(stones)
        
        while stones:
            most_heaviest_stone = heapq.heappop(stones)
            if not stones:
                return abs(most_heaviest_stone)
            
            second_heaviest_stone = heapq.heappop(stones)
            
            # Only append the smashed stone if it's not 0.
            smashed_stone = most_heaviest_stone - second_heaviest_stone if most_heaviest_stone != second_heaviest_stone else 0
            if smashed_stone:
                heapq.heappush(stones, smashed_stone)
            
        return 0
