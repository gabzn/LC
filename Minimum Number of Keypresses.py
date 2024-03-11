https://leetcode.com/problems/minimum-number-of-keypresses/

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counter = Counter(s)
        every_nine = 0
        multiplier = 1
        res = 0
        
        for char, freq in sorted(counter.items(), key=lambda p: -p[1]):
            res += (freq * multiplier)
            every_nine += 1
            
            if every_nine % 9 == 0:
                multiplier += 1
                every_nine = 0
            
        return res
