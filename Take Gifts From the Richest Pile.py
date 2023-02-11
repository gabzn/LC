https://leetcode.com/problems/take-gifts-from-the-richest-pile/
  
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:            
        gifts = [-gift for gift in gifts]
        heapify(gifts)
        
        while k:
            max_gift = -heapq.heappop(gifts)
            heapq.heappush(gifts, -math.floor(math.sqrt(max_gift)))
            k -= 1
    
        return -sum(gifts)
