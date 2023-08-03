https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        LEN = len(nums)
        target = [] * LEN
        
        for idx in range(LEN):
            value = nums[idx]
            corresponding_index = index[idx]
            target.insert(corresponding_index, value)
        
        return target
