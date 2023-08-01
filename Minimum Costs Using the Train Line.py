https://leetcode.com/problems/minimum-costs-using-the-train-line/

class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], express_cost: int) -> List[int]:
        LEN = len(regular)
        res = [0] * LEN
        
        dp = [[0 for _ in range(LEN + 1)] for _ in range(2)]
        dp[0][0] = 0                # The initial cost to take the regular train at stop 0 is 0 because that's where we begin
        dp[1][0] = express_cost     # The initial cost to take the express train at stop 0 is express_cost because we need to pay to upgrade
        
        """
        what is the min cost to reach stop i
        stop i = min( (stop i, regular), (stop i, express) )
            (stop i, regular) = min( (stop i - 1, regular) + regular[i], (stop i - 1, express) + regular[i])
            (stop i, express) = min( (stop i - 1, regular) + express_cost + express[i], (stop - 1, express) + express[i] ) 
        """
        for index in range(1, LEN + 1):
            dp[0][index] = regular[index - 1] + min(dp[0][index - 1], dp[1][index - 1])
            dp[1][index] = express[index - 1] + min(dp[0][index - 1] + express_cost, dp[1][index - 1])
            res[index - 1] = min(dp[0][index], dp[1][index])
        
        return res
