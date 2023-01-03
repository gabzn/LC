https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
  
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        
        for row_ind in range(len(mat)):
            ones = 0    
            for col_ind in range(len(mat[row_ind])):
                if mat[row_ind][col_ind] == 1:
                    ones += 1
        
            mat[row_ind] = (ones, row_ind)
            
        heapify(mat)
        
        while mat and len(ans) < k:
            _, ind = heappop(mat)
            ans.append(ind)
            
        return ans
