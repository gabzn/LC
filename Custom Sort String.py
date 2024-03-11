https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        res = []
        
        for char in order:
            if char in counter:
                freq = counter[char]
                for _ in range(freq):
                    res.append(char)
                
                del counter[char]
        
        for char, freq in counter.items():
            for _ in range(freq):
                res.append(char)
            
        return ''.join(res)
