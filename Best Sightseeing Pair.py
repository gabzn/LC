https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        values[i] + values[j] + i - j
        (values[i] + i) + (values[j] - j)
                           values[j] > j
                                i         
        vals:             8 1 5 2  6
        idxs:             0 1 2 3  4
        max_diffs:        3 3 2 2  2
        """
        N = len(values)
        max_diff_after_i = [0] * N
        max_diff_after_i[-1] = values[-1] - (N - 1)
        for i in range(N - 2, -1, -1):
            prev_diff = values[i + 1] - (i + 1)
            max_diff_after_i[i] = max(max_diff_after_i[i + 1], prev_diff)

        res = 0
        for i in range(N - 1):
            # (values[j] - j) = max_diff_after_i[i]
            res = max(res, (values[i] + i) + max_diff_after_i[i])
        return res
