https://leetcode.com/problems/minimum-number-of-frogs-croaking/
https://www.youtube.com/watch?v=h46eoBqgArY&pp=ygUgTWluaW11bSBOdW1iZXIgb2YgRnJvZ3MgQ3JvYWtpbmc%3D

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = res = 0

        for char in croakOfFrogs:
            if char == 'c':
                c += 1
                
            if char == 'r':
                r += 1
                c -= 1
                if c < 0:
                    return -1
                
            if char == 'o':
                o += 1
                r -= 1
                if r < 0:
                    return -1
                
            if char == 'a':
                a += 1
                o -= 1
                if o < 0:
                    return -1
            
            if char == 'k':
                a -= 1
                if a < 0:
                    return -1
            
            res = max(res, c + r + o + a)
        
        if c + r + o + a > 0:
            return -1
        
        return res
