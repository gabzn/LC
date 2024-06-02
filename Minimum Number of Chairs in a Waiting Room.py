https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs = 0
        free = 0
        
        for char in s:
            if char == "E":
                if free == 0:
                    chairs += 1
                else:
                    free -= 1
            else:
                free += 1
                
        return chairs
