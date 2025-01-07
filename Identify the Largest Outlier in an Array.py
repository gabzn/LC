https://leetcode.com/classic/problems/identify-the-largest-outlier-in-an-array/description/

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        def is_outlier(num):
            diff = total - num
            if diff % 2 == 1:
                return False
            half_of_diff = diff // 2
            if half_of_diff in num_to_indices:
                return True if num != half_of_diff else len(num_to_indices[half_of_diff]) > 1

        total = 0        
        num_to_indices = defaultdict(list)
        for index, num in enumerate(nums):
            total += num
            num_to_indices[num].append(index)

        res = -1001
        for num in nums:
            if is_outlier(num):
                res = max(res, num)

        return res
