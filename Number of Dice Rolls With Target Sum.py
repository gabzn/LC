https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
  
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        # dp(dice, remaining) returns the number of way to make up remaining when we have n number of dice
        def dp(dice, remaining, memo):
            # when we have no more dice and the remaining is also 0, that means we found 1 way
            if dice == 0 and remaining == 0:
                return 1
            # when we have no more dice but remaining is not 0, that means there's no way we can make it
            if dice == 0:
                return 0 
            if (dice, remaining) in memo:
                return memo[(dice, remaining)]
            
            memo[(dice, remaining)] = 0
            for face_value in range(1, k + 1):
                if face_value <= remaining:
                    memo[(dice, remaining)] += dp(dice - 1, remaining - face_value, memo)    
            
            return memo[(dice, remaining)] % ((10 ** 9) + 7)
      
        return dp(n, target, {})  
