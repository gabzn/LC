https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

class Solution:
    def getWordsInLongestSubsequence(self, LEN: int, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        
        for idx in range(1, LEN):
            if groups[idx] != groups[idx - 1]:
                res.append(words[idx])
        
        return res
