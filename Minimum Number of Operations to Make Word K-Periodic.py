https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        N = len(word)
        parts = N // k
        
        counter = Counter()
        for i in range(k - 1, N, k):
            counter[word[i-k+1: i+1]] += 1
            
        return parts - max(counter.values())
