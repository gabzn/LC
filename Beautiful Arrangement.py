https://leetcode.com/problems/beautiful-arrangement/

class Solution:
    def countArrangement(self, n: int) -> int:
        res = [0]
        self.backtrack(n, 1, set(), res)
        return res[0]
    
    def backtrack(self, n, val, perm, res):
        if val > n:
            res[0] += 1
            return
        
        for idx in range(1, n + 1):
            if idx in perm:
                continue
            
            if idx % val == 0 or val % idx == 0:
                perm.add(idx)
                self.backtrack(n, val + 1, perm, res)
                perm.remove(idx)
        
        return
