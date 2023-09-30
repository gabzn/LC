https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)

        res = 0
        for _, count in counter.items():            
            if count == 1:
                return -1
            
            res += (count + 2) // 3
                    
        return res
