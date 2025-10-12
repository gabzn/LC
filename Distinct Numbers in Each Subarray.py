https://leetcode.com/problems/distinct-numbers-in-each-subarray/

from collections import defaultdict

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = defaultdict(int)
        
        for i, num in enumerate(nums):
            counter[num] += 1

            left = i + 1 - k
            if left < 0:
                continue

            res.append(len(counter))

            counter[nums[left]] -= 1
            if counter[nums[left]] == 0:
                del counter[nums[left]]

        return res
