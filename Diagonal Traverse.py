https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        M, N = map(len, [mat, mat[0]])
        
        res = []
        ordering = defaultdict(list)
        
        for i in range(M):
            for j in range(N):
                ordering[i + j].append(mat[i][j])
        
        need_reverse = True
        for i in range(len(ordering)):
            nums = reversed(ordering[i]) if need_reverse else ordering[i]
            
            for num in nums:
                res.append(num)
            
            need_reverse = not need_reverse
            
        return res
