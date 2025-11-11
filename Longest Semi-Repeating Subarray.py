https://leetcode.com/problems/longest-semi-repeating-subarray

class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        repeated_elements = set()
        res = 0
        left = 0

        for right, num in enumerate(nums):
            counter[num] += 1

            # Occurs at least twice, it's a repeated element now.
            if counter[num] == 2:
                repeated_elements.add(num)
            
            while len(repeated_elements) > k:
                to_remove = nums[left]
                # It is currently 2 and we are going to subtract it to 1 so it's not repeating.
                if counter[to_remove] == 2:
                    repeated_elements.remove(to_remove)

                counter[to_remove] -= 1
                if counter[to_remove] == 0:
                    del counter[to_remove]

                left += 1

            res = max(res, right - left + 1)

        return res
