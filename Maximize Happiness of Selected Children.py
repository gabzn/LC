https://leetcode.com/problems/maximize-happiness-of-selected-children/

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        N = len(happiness)

        happiness.sort(reverse=True)
        res = decrementals = 0
        
        for idx in range(min(k, N)):
            res += max((happiness[idx] + decrementals), 0)
            decrementals -= 1
        
        return res
