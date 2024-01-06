https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/discuss/4518474/Beginner-Friendly-or-Memoization-or-Simple-Recursion-based-on-choices-or-C%2B%2B-or-Explained-or-Beats-100
https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @cache
        def dp(x):
            if x <= y:
                return y - x
            
            res = math.inf
            
            if x % 5 == 0:
                res = min(res, 1 + dp(x // 5))
            else:
                diff_to_make_x_divisible_by_five = 5 - (x % 5)
                x_prime = x + diff_to_make_x_divisible_by_five
                
                res = min(res, diff_to_make_x_divisible_by_five + 1 + dp(x_prime // 5))
            
            if x % 11 == 0:
                res = min(res, 1 + dp(x // 11))
            else:
                diff_to_make_x_divisible_by_eleven = 11 - (x % 11)
                x_prime = x + diff_to_make_x_divisible_by_eleven
                
                res = min(res, diff_to_make_x_divisible_by_eleven + 1 + dp(x_prime // 11))
            
            res = min(res, 1 + dp(x - 1))
            
            return res
        
        return dp(x)
