https://leetcode.com/problems/combination-sum-iii/
  
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.find_combinations(k, n, 1, [], [])
        
    def find_combinations(self, k, target, start, cur, res):      
        if len(cur) == k:
            if target == 0:
                res.append(cur[:])
            return res
        
        for num in range(start, 10):
            cur.append(num)
            res = self.find_combinations(k, target - num, num + 1, cur, res)
            cur.pop()    
        
        return res
