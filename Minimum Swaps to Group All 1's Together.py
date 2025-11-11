https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # All 1's together means a window of a certain size
        window_size = data.count(1)
        if window_size == 0:
            return 0
        res = inf
        zeroes = 0

        for right, num in enumerate(data):
            zeroes += (num == 0)

            left = right + 1 - window_size
            if left < 0:
                continue

            res = min(res, zeroes)
            zeroes -= (data[left] == 0)

        return res
