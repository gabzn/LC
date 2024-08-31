https://leetcode.com/problems/find-the-key-of-the-numbers/

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1, num2, num3 = map(str, [num1, num2, num3])
        while len(num1) != 4:
            num1 = "0" + num1
        while len(num2) != 4:
            num2 = "0" + num2
        while len(num3) != 4:
            num3 = "0" + num3
            
        res = ''
        for i in range(4):
            res += str(min(map(int, [num1[i], num2[i], num3[i]])))
        return int(res)
