https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/

class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        def is_num_common(num):
            for i in range(1, N):
                nums = arrays[i]
                j = bisect_left(nums, num)
                if j == len(nums) or nums[j] != num:
                    return False
            return True

        N = len(arrays)
        res = []

        for num in arrays[0]:
            if is_num_common(num):
                res.append(num)

        return res
