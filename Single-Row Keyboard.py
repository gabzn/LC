https://leetcode.com/problems/single-row-keyboard/

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        res = previous = 0
        
        for char in word:
            current = keyboard.index(char)
            res += abs(current - previous)
            previous = current
        
        return res
