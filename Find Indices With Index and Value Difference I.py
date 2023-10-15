https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        LEN = len(nums)
        ans = [-1, -1]
        
        for i in range(LEN):
            for j in range(LEN):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    ans = [i, j]
        
        return ans
