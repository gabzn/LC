https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        complement = {0: 0}
        res = 0
        
        for index in range(len(time)):
            time[index] = time[index] % 60
        
        for t in time:
            if t == 0:
                res += complement[0]
                complement[0] += 1
                continue
                
            # Two-sum
            if t != 0 and t in complement:
                res += complement[t]
            complement[60 - t] = complement.setdefault(60 - t, 0) + 1
            
        return res
