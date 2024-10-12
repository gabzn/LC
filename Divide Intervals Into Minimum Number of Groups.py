https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

"""
1          5
1                     10
   2   3
           5          10
             6      8
"""
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:        
        groups = []

        for start, end in sorted(intervals):
            if groups and start > groups[0]:
                heappop(groups)

            heappush(groups, end)

        return len(groups)
