https://leetcode.com/problems/count-tested-devices-after-test-operations/

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        LEN = len(batteryPercentages)
        res = 0
        
        for i in range(LEN):
            if batteryPercentages[i] == 0:
                continue
            
            res += 1
            for j in range(i + 1, LEN):
                if batteryPercentages[j] > 0:
                    batteryPercentages[j] -= 1
        
        return res
