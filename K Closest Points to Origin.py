https://leetcode.com/problems/k-closest-points-to-origin/
  
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:                
        heap = []
        
        for index, pair in enumerate(points):
            x, y = pair
            distance = x * x + y * y      
            
            if len(heap) == k and -heap[0][0] > distance:
                heappop(heap)
                heappush(heap, (-distance, index))
            
            if len(heap) < k:
                heappush(heap, (-distance, index))
        
        return [points[index] for _, index in heap]
