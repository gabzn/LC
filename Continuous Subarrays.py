https://leetcode.com/problems/continuous-subarrays/description/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = 0
        left = 0
        counter = Counter()

        for right, num in enumerate(nums):
            counter[num] += 1

            # We only care about the max and min in the window.
            # If the diff between max and min > 2, we start removing num from left.
            # counter has at most 4 elements
            # 1, 2, 3, 4
            while max(counter) - min(counter) > 2:
                to_remove = nums[left]
                counter[to_remove] -= 1
                if counter[to_remove] == 0:
                    del counter[to_remove]

                left += 1

            res += (right - left + 1) 

        return res
