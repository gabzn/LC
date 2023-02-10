https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
  
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = math.inf
        l, w_blocks = 0, 0
        
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                w_blocks += 1
            
            if r - l + 1 == k:
                res = min(res, w_blocks)
                
                if blocks[l] == 'W':
                    w_blocks -= 1
                    
                l += 1
        
        return res if res != math.inf else 0
