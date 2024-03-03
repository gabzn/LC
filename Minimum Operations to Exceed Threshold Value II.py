https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        heapify(nums)
        
        while len(nums) >= 2:
            x = heappop(nums)
            if x >= k:
                break
            
            y = heappop(nums)
            
            heappush(nums, min(x, y) * 2 + max(x, y))
            res += 1
        
        return res
