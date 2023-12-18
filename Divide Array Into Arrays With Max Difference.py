https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        LEN = len(nums)
        
        nums.sort()
        res = []
        
        for i in range(2, LEN, 3):
            if nums[i] - nums[i-2] <= k:
                res.append(nums[i-2: i+1])
            else:
                return []
        
        return res
