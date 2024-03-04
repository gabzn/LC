https://leetcode.com/problems/bag-of-tokens/

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:        
        tokens.sort()
      
        score = res = 0
        l, r = 0, len(tokens) - 1
        
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
            elif score >= 1:
                power += tokens[r]
                score -= 1
                r -= 1                
            else:
                return res
            
            res = max(res, score)                

        return res
