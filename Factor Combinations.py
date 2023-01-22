https://leetcode.com/problems/factor-combinations/
  
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        return self.backtrack(n, 2, [], [])
    
    def backtrack(self, n, start, current, res):
        if n == 1:
            if len(current) > 1:
                res.append(current.copy())
            return res
        
        for factor in range(start, n + 1):
            if n % factor == 0:
                current.append(factor)
                res = self.backtrack(n // factor, factor, current, res)
                current.pop()
        
        return res
