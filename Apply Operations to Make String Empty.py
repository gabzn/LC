https://leetcode.com/problems/apply-operations-to-make-string-empty/

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counter = Counter(s)
        max_freq = max(counter.values())
        
        for char, freq in counter.items():
            if freq != max_freq:
                counter[char] = 0
        
        res = []
        
        for char in s:
            if counter[char] != 0:
                if counter[char] == 1:
                    res.append(char)
                else:
                    counter[char] -= 1
        
        return "".join(res)
