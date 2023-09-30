https://leetcode.com/problems/minimum-operations-to-collect-elements/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        LEN = len(nums)
        nums.reverse()
        
        for idx in range(LEN):
            found = True
            
            for j in range(1, k+1):
                if j not in nums[:idx+1]:
                    found = False
                    break
                
            if found:
                return idx + 1
