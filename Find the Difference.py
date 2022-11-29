https://leetcode.com/problems/find-the-difference/
  
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        
        letter_counts = [0] * 26
        
        for letter in s:
            ind = ord(letter) - ord('a')
            letter_counts[ind] += 1
            
        for letter in t:
            ind = ord(letter) - ord('a')
            if letter_counts[ind] == 0:
                return letter
            
            letter_counts[ind] -= 1
