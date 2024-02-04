https://leetcode.com/problems/ant-on-the-boundary/

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        res = p = 0
        
        for num in nums:
            p += num
            if p == 0:
                res += 1
        
        return res
