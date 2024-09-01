https://leetcode.com/problems/k-th-nearest-obstacle-queries/

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        res, heap = [], []
        
        for x, y in queries:
            distance = abs(x) + abs(y)
            heappush(heap, -distance)
            if len(heap) > k:
                heappop(heap)
            
            res.append(-heap[0] if len(heap) == k else -1)
        
        return res
