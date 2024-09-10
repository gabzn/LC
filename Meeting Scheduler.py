https://leetcode.com/problems/meeting-scheduler/

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        i = j = 0

        while i < len(slots1) and j < len(slots2):
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]

            latest_start = max(s1, s2)
            earliest_end = min(e1, e2)

            if earliest_end - latest_start >= duration:
                return [latest_start, latest_start + duration]

            if e1 < e2:
                i += 1
            else:
                j += 1

        return []
