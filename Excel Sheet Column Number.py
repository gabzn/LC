https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res, power = 0, len(columnTitle) - 1
        
        for char in columnTitle:
            val = ord(char) - ord('A') + 1
            res += (val * (26 ** power))
            power -= 1
        
        return res
