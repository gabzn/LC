https://leetcode.com/problems/combination-sum-iii/
  
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.backtrack(k, n, 1, [], [])
    
    def backtrack(self, k, n, start, current, res):
        if len(current) == k:
            if n == 0:
                res.append(current.copy())
            return res
        
        for i in range(start, 10):   
            current.append(i)
            res = self.backtrack(k, n - i, i + 1, current, res)
            current.pop()
            
        return res
