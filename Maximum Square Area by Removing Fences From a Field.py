https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hfs: List[int], vfs: List[int]) -> int:        
        MOD = 10 ** 9 + 7
      
        h = sorted([1] + hfs + [m])
        v = sorted([1] + vfs + [n])
        
        existing_widths = set()
        
        # Go through the horizontal fences (up down) and compute the distances between every single pair of fences
        for bottom in range(len(h)):
            for top in range(bottom):
                width = h[bottom] - h[top]
                existing_widths.add(width)
        
        res = 0
        
        # Go through the vertical fences (left right) and compute the distances between every single pair of fences
        for right in range(len(v)):
            for left in range(right):
                width = v[right] - v[left]
                
                if width in existing_widths:
                    res = max(res, width * width)
        
        return res % MOD if res != 0 else -1
