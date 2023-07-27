https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        LEN = len(questions)
        
        def dp(index, memo):
            if index >= LEN:
                return 0
            if index in memo:
                return memo[index]
            
            pts, power = questions[index]
            
            solve = pts + dp(index + power + 1, memo)
            skip = dp(index + 1, memo)
            
            memo[index] = max(solve, skip)
            return memo[index]
            
        return dp(0, {})
