https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description/

class Solution:
    def maxFreeTime(self, total_time: int, k: int, start: List[int], end: List[int]) -> int:
        gap_sizes = []
        for i in range(len(start)):
            if i == 0:
                gap_sizes.append(start[i])
            else:
                gap_size = start[i] - end[i - 1]
                gap_sizes.append(gap_size)
        gap_sizes.append(total_time - end[-1])

        res = free_time = 0

        for i in range(len(gap_sizes)):
            free_time += gap_sizes[i]

            if i < k:
                continue

            res = max(res, free_time)
            free_time -= gap_sizes[i - k]

        return res
