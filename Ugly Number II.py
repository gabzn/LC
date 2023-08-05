https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [1]
        prime_2, prime_3, prime_5 = 0, 0, 0

        # The intuition is that next ugly number is just the min among SOME previous numbers multiplied by the factor 2, 3, 5
        # Initially, all three point to the first number which has the value of 1
        # Multiply the value each pointer points to and get the min, this min will be the next ugly number. Move pointers accordingly.
        for _ in range(n):
            next_prime_with_2 = ugly_nums[prime_2] * 2
            next_prime_with_3 = ugly_nums[prime_3] * 3
            next_prime_with_5 = ugly_nums[prime_5] * 5
            
            next_ugly_num = min(next_prime_with_2, next_prime_with_3, next_prime_with_5)
            ugly_nums.append(next_ugly_num)
            
            if next_ugly_num == next_prime_with_2:
                prime_2 += 1
            if next_ugly_num == next_prime_with_3:
                prime_3 += 1
            if next_ugly_num == next_prime_with_5:
                prime_5 += 1
        
        return ugly_nums[n - 1]
