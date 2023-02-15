https://leetcode.com/problems/add-to-array-form-of-integer/
  
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_combined = 0
        for n in num:
            num_combined *= 10
            num_combined += n
        
        num_combined += k

        res = []
        for n in str(num_combined):
            res.append(int(n))
        
        return res
