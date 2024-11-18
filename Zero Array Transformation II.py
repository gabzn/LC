https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def can_get_zero_array_with_first_k_queries(k):
            lst = [0] * (N + 1)
            for i in range(k):
                l, r, val = queries[i]
                lst[l] += val
                lst[r + 1] -= val

            for i in range(1, N + 1):
                lst[i] += lst[i - 1]

            for i in range(N):
                if lst[i] < nums[i]:
                    return False

            return True
        
        N = len(nums)
        Q = len(queries)
        res = inf
        left = -1
        right = Q + 1

        while left + 1 != right:
            k = (left + right) // 2
            if can_get_zero_array_with_first_k_queries(k):
                res = k
                right = k
            else:
                left = k
    
        return res if res != inf else -1
