https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

class Solution:
    def smallestChair(self, times: List[List[int]], target: int) -> int:
        free = []
        taken = []

        for i in range(len(times)):
            heappush(free, i)

        for i, [s, e] in enumerate(times):
            times[i] = [s, e, i]

        for s, e, i in sorted(times):
            while taken and taken[0][0] <= s:
                _, idle_chair = heappop(taken)
                heappush(free, idle_chair)

            smallest_available_chair = heappop(free)
            if i == target:
                return smallest_available_chair

            heappush(taken, (e, smallest_available_chair))
