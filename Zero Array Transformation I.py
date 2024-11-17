https://leetcode.com/problems/zero-array-transformation-i/

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        lst = [0] * (N + 1)

        for l, r in queries:
            lst[l] += 1
            lst[r + 1] -= 1

        for i in range(1, N + 1):
            lst[i] += lst[i - 1]

        for i in range(N):
            if lst[i] < nums[i]:
                return False

        return True
