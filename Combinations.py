https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(start, current, res):
            if len(current) == k:
                res.append(current.copy())
                return res
            
            for num in range(start, n + 1):
                current.append(num)
                res = backtrack(num + 1, current, res)
                current.pop()
            
            return res
        return backtrack(1, [], [])
------------------------------------------------------
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.backtrack(n, k, 1, [], [])
    
    def backtrack(self, n, k, ind, current, res):
        if len(current) == k:
            res.append(current.copy())
            return res
        
        for i in range(ind, n + 1):
            current.append(i)
            res = self.backtrack(n, k, i + 1, current, res)
            current.pop()
        
        return res
