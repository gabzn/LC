https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        N = len(hours)
        remainder_dict = defaultdict(int)
        res = 0
    
        for h in hours:
            h %= 24
            
            if h == 0:
                res += remainder_dict[h]
            else:
                res += remainder_dict[24 - h]
            
            remainder_dict[h] += 1
                
        return res
