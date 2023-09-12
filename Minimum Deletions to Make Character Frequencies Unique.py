https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = list(Counter(s).values())
        frequencies.sort(reverse=True)
        
        res = 0
        unique_freq = set()
        
        for i in range(len(frequencies)):
            if frequencies[i] not in unique_freq:
                unique_freq.add(frequencies[i])
            else:
                while frequencies[i] in unique_freq:
                    frequencies[i] -= 1
                    res += 1
                if frequencies[i] != 0:
                    unique_freq.add(frequencies[i])
            
        return res
----------------------------------------------------------------------------------------
class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = list(Counter(s).values())
        frequencies.sort(reverse=True)
        
        res = 0
        unique_freq = set()
        
        for i in range(len(frequencies)):
            while frequencies[i] in unique_freq:
                frequencies[i] -= 1
                res += 1
            
            if frequencies[i] != 0 and frequencies[i] not in unique_freq:
                unique_freq.add(frequencies[i])
    
        return res
