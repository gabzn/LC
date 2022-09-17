Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Input: x = 123
Output: 321
  
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = True if x < 0 else False
        x = abs(x)
        
        new_x = 0
        MAX_VAL = (2 ** 31) - 1
        
        while x != 0:
            last_digit = x % 10
            x = x // 10
                        
            if new_x > (MAX_VAL // 10) or (new_x == MAX_VAL // 10 and last_digit >= MAX_VAL % 10):
                return 0
            new_x = (new_x * 10) + last_digit

        if is_negative:
            return -new_x
        return new_x
