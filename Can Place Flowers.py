https://leetcode.com/problems/can-place-flowers/
  
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        for ind, plot in enumerate(flowerbed):
            if plot == 0:                
                is_left_empty = (ind == 0) or (flowerbed[ind-1] != 1)
                is_right_empty = (ind == len(flowerbed)-1) or (flowerbed[ind+1] != 1)
                
                if is_left_empty and is_right_empty:
                    flowerbed[ind] = 1
                    n -= 1   
                    if not n:
                        return True
                    
        return False
