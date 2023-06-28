https://leetcode.com/problems/toss-strange-coins/

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        LEN = len(prob)

        def dp(index, heads, memo):
            # If we have more heads than we need, return 0
            if heads > target:
                return 0
            
            # After tossing all of the coins, if we get the required number of heads,
            # return 1 to count this case, otherwise return 0.
            if index == LEN:
                return 1 if heads == target else 0
            
            if (index, heads) in memo:
                return memo[index, heads]
            
            prob_of_getting_head = prob[index] * dp(index + 1, heads + 1, memo)
            prob_of_not_getting_head = (1 - prob[index]) * dp(index + 1, heads, memo)
            
            memo[index, heads] = prob_of_getting_head + prob_of_not_getting_head
            return memo[index, heads]

        return dp(0, 0, {})
