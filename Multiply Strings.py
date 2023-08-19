https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def mul(shorter, longer):
            res = ''
            carry = 0
            
            for digit in longer:
                product = (int(shorter) * int(digit)) + carry
                
                last_digit = product % 10
                carry = product // 10
                
                res += str(last_digit)
            
            if carry:
                res += str(carry)
            
            return int(res[::-1])
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        product = 0
        for index, num in enumerate(num1):
            product += mul(num, num2) * (10 ** index)
            
        return str(product)
