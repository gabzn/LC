https://leetcode.com/problems/gas-station/
https://www.youtube.com/watch?v=ROrEAUbWg9w

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total_gas, start = 0, 0
        
        for i in range(len(gas)):
            total_gas += (gas[i] - cost[i])
            
            if total_gas < 0:
                total_gas = 0
                start = i + 1
            
        return start
