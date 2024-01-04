https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        
        res = cur_weight = 0
        
        for w in weight:
            cur_weight += w
            if cur_weight > 5000:
                return res
            res += 1
        
        return res
