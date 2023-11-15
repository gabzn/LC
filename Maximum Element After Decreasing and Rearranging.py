https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        LEN = len(arr)
        
        arr.sort()
        if arr[0] != 1:
            arr[0] = 1
        
        res = 1
        for idx in range(1, LEN):
            if abs(arr[idx] - arr[idx - 1]) <= 1:
                res = max(res, arr[idx])
            else:
                arr[idx] = arr[idx - 1] + 1
                res = max(res, arr[idx])
        
        return res
