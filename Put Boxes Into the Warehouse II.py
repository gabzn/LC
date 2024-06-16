https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        N = len(warehouse)

        pref = [inf] * N
        pref[0] = warehouse[0]
        for i in range(1, N):
            pref[i] = min(pref[i-1], warehouse[i])

        suff = [inf] * N
        suff[-1] = warehouse[-1]
        for i in range(N - 2, -1, -1):
            suff[i] = min(suff[i+1], warehouse[i])

        maxes = sorted([max(left, right) for left, right in zip(pref, suff)])
        boxes.sort()
        j = res = 0

        for i in range(N):
            if j < len(boxes) and boxes[j] <= maxes[i]:
                j += 1
                res += 1

        return res
