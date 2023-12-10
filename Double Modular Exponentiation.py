https://leetcode.com/problems/double-modular-exponentiation/

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        LEN = len(variables)
        res = []
        
        for idx, [a, b, c, m] in enumerate(variables):
            if (((a ** b) % 10) ** c) % m == target:
                res.append(idx)
      
        return res
