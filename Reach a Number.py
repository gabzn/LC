https://leetcode.com/problems/reach-a-number/
https://leetcode.com/problems/reach-a-number/discuss/112968/Short-JAVA-Solution-with-Explanation

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        step, sum = 0, 0
        
        while sum < target or (sum - target) % 2 != 0:
            step += 1
            sum += step
            
        return step
