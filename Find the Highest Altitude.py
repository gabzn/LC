https://leetcode.com/problems/find-the-highest-altitude/
  
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_alt = max(0, gain[0])
        
        for ind in range(1, len(gain)):
            gain[ind] += gain[ind-1]
            highest_alt = max(highest_alt, gain[ind])
        
        return highest_alt
