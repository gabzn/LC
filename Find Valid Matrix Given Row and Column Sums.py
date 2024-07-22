https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

class Solution:
    def restoreMatrix(self, row_sum: List[int], col_sum: List[int]) -> List[List[int]]:
        ROWS = len(row_sum)
        COLS = len(col_sum)
        
        res = [[0] * COLS for _ in range(ROWS)]
        for i in range(ROWS):
            for j in range(COLS):
                val = min(row_sum[i], col_sum[j])
                res[i][j] = val
                row_sum[i] -= val
                col_sum[j] -= val
        
        return res
---------------------------------------------------------------------------------------
class Solution:
    def restoreMatrix(self, row_sum: List[int], col_sum: List[int]) -> List[List[int]]:
        res = [[0 for _ in range(len(col_sum))] for _ in range(len(row_sum))]
        row_heap = [(num, i) for i, num in enumerate(row_sum)]
        col_heap = [(num, i) for i, num in enumerate(col_sum)]
        heapify(row_heap)
        heapify(col_heap)
        
        while row_heap:
            row_num, i = heappop(row_heap)
            col_num, j = heappop(col_heap)
            
            to_insert = min(row_num, col_num)
            res[i][j] = to_insert
            
            row_num -= to_insert
            col_num -= to_insert
            
            if row_num:
                heappush(row_heap, (row_num, i))
            if col_num:
                heappush(col_heap, (col_num, j))
            
        return res
