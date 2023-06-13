https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
https://www.youtube.com/watch?v=qkDTtfnQUJU
  
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        res, heap = 0, []
        
        for row in range(N):
            heap.append((matrix[row][0], row, 0))
        heapify(heap)
        
        while k:
            res, row, col = heappop(heap)            
            if col < N - 1:
                heappush(heap, (matrix[row][col + 1], row, col + 1))
            
            k -= 1

        return res  
