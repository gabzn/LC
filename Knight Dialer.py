https://leetcode.com/problems/knight-dialer/
  
class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        # next_digits[i] tells us what digits we can reach next from i
        # next_digits = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        
        for _ in range(n-1):
            digit_counts = [0] * 10
            
            digit_counts[0] = dp[4] + dp[6]
            digit_counts[1] = dp[6] + dp[8]
            digit_counts[2] = dp[7] + dp[9]
            digit_counts[3] = dp[4] + dp[8]
            digit_counts[4] = dp[3] + dp[9] + dp[0]
            digit_counts[5] = 0
            digit_counts[6] = dp[1] + dp[7] + dp[0]
            digit_counts[7] = dp[2] + dp[6]
            digit_counts[8] = dp[1] + dp[3]
            digit_counts[9] = dp[2] + dp[4]
            
            dp = digit_counts
            
        return sum(dp) % (10**9+7)

--------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 1000000007
        dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        # next_digits[i] tells us what digits we can reach next from i
        # next_digits = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        
        for _ in range(n-1):
            digit_counts = [0] * 10
            
            digit_counts[0] = (dp[4] + dp[6]) % MOD
            digit_counts[1] = (dp[6] + dp[8]) % MOD
            digit_counts[2] = (dp[7] + dp[9]) % MOD
            digit_counts[3] = (dp[4] + dp[8]) % MOD
            digit_counts[4] = (dp[3] + dp[9] + dp[0]) % MOD
            digit_counts[5] = 0
            digit_counts[6] = (dp[1] + dp[7] + dp[0]) % MOD
            digit_counts[7] = (dp[2] + dp[6]) % MOD
            digit_counts[8] = (dp[1] + dp[3]) % MOD
            digit_counts[9] = (dp[2] + dp[4]) % MOD
                              
            dp = digit_counts
            
        return sum(dp) % MOD
    
#         MOD = 1000000007
        
#         # next_digits[i] tells us what digits we can reach next from i
#         next_digits = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        
#         cur_n_digits_counts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        
#         # n - 1 iterations
#         for _ in range(n-1):
#             next_n_digits_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            
#             # Go through 0 - 9
#             for current_digit in range(10):
#                 # Find what digits we can reach next from current_digits (0-9)
#                 for next_digit in next_digits[current_digit]:
#                     next_n_digits_counts[next_digit] = (cur_n_digits_counts[current_digit] + next_n_digits_counts[next_digit]) % MOD
                    
#             cur_n_digits_counts = next_n_digits_counts
        
#         return sum(cur_n_digits_counts) % MOD    
