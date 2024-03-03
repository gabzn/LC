https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        for i in range(2, N):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        
        return arr1 + arr2
