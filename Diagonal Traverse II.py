https://leetcode.com/problems/diagonal-traverse-ii/

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        ordering = defaultdict(list)
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                ordering[i + j].append(nums[i][j])
        
        for i in range(len(ordering)):
            nums = ordering[i]
            while nums:
                res.append(nums.pop())
        
        return res
