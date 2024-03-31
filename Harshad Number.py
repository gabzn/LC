https://leetcode.com/problems/harshad-number/

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x_str = str(x)
        s = 0
        for d in x_str:
            s += int(d)
            
        return s if x % s == 0 else -1
