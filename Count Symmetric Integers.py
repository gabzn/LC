https://leetcode.com/problems/count-symmetric-integers/

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        
        for num in range(low, high + 1):
            num = str(num)
            size = len(num)
            if size % 2 == 1:
                continue
            
            digit_sum = 0
            for i in range(size):
                digit = num[i]
                if i < size // 2:
                    digit_sum += int(digit)
                else:
                    digit_sum -= int(digit)
            
            res += digit_sum == 0
        
        return res        
