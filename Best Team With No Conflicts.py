https://leetcode.com/problems/best-team-with-no-conflicts/

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_score_pair = [pair for pair in zip(ages, scores)]
        age_score_pair.sort()            
        
        def dp(index, prev_score, memo):
            if index == len(age_score_pair):
                return 0
            if (index, prev_score) in memo:
                return memo[(index, prev_score)]
            
            skip = dp(index + 1, prev_score, memo)

            pick = 0
            _, score = age_score_pair[index]
            if score >= prev_score:
                pick = score + dp(index + 1, score, memo)
                
            memo[(index, prev_score)] = max(pick, skip)
            return memo[(index, prev_score)]
        
        return dp(0, 0, {})
