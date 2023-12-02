https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hbs: List[int], vbs: List[int]) -> int:
        def compute_max_len(bars):
            LEN = len(bars)
            side_len = 1
            
            i = 0
            while i < LEN:
                j = i
                
                # Find the longest consecutive sequence of bars
                while j < LEN - 1 and bars[j] + 1 == bars[j + 1]:
                    j += 1
                
                # Removing the longest consecutive sequence of bars
                side_len = max(side_len, bars[j] - bars[i] + 2)        
                i = j + 1    
            
            return side_len
            
        hbs.sort()
        vbs.sort()
        
        # Since we want to compute the area of a square, the side length is bounded by the min between length and width
        max_side_len = min(compute_max_len(hbs), compute_max_len(vbs))
        return max_side_len ** 2
