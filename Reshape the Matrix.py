https://leetcode.com/problems/reshape-the-matrix/
  
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        if M * N != r * c:
            return mat
        
        deque = collections.deque()
        for i in range(M):
            for j in range(N):
                deque.append(mat[i][j])
                
        res = [[] for i in range(r)]
        for i in range(r):
            for j in range(c):
                res[i].append(deque.popleft())
    
        return res
