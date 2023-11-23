https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check_is_arithmetic(arr):
            arr.sort()
            diff = arr[1] - arr[0]
            
            for i in range(1, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    return False
                
            return True
        
        res = []

        for li, ri in zip(l, r):
            res.append(check_is_arithmetic(nums[li: ri + 1]))
        
        return res
