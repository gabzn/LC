https://leetcode.com/problems/find-if-array-can-be-sorted/

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        N = len(nums)
        segments = []
        left = right = 0

        while right < N:
            segment = []

            while right < N and nums[right].bit_count() == nums[left].bit_count():
                segment.append(nums[right])
                right += 1

            segment.sort()
            segments.append(segment)
            left = right

        for i in range(1, len(segments)):
            prev_max = segments[i - 1][-1]
            cur_min = segments[i][0]
            if prev_max > cur_min:
                return False

        return True
