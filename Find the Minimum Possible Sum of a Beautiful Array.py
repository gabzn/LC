https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        no_good = set()
        res = []
                    
        for num in range(1, target + 1):
            if len(res) == n:
                break
            if num in no_good:
                continue
            
            res.append(num)
            no_good.add(target - num)
            
        while len(res) < n:
            target += 1
            if target not in no_good:
                res.append(target)
                
        return sum(res)
