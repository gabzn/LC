https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        
        cache = [0] * (N + 1)
        cache[1] = 1
        
        for i in range(2, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[N]
-----------------------------------------------------------
class Solution:
    def fib(self, n: int) -> int:
        
        def dp(n, memo):
            if n == 0 or n == 1:
                return n
            if n in memo:
                return memo[n]
            
            memo[n] = dp(n - 1, memo) + dp(n - 2, memo)
            return memo[n]
        
        return dp(n, {})
