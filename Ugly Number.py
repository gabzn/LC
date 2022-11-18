https://leetcode.com/problems/ugly-number/
  
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        # Keep dividing n by each prime num as long as the remainder is 0.
        prime_nums = [2, 3, 5]
        for prime_num in prime_nums:
            while n % prime_num == 0:
                n = n // prime_num
        
        return n == 1
