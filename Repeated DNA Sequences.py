https://leetcode.com/problems/repeated-dna-sequences/
  
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        res, unique_sequences = set(), set()
        l = 0
        
        for r in range(9, len(s)):
            substr = s[l: r + 1]
            if substr in unique_sequences:
                res.add(substr)
            
            unique_sequences.add(substr)
            l += 1
        
        return list(res)
