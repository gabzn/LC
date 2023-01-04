https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
  
from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        rounds = 0
                    
        for _, count in counter.items():
            if count == 1:
                return -1
            
            if count % 3 == 0:
                rounds += count // 3
            else:
                rounds += (count // 3) + 1
        
        return rounds
