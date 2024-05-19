https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        num_len = len(str(nums[0]))
        nums = [str(num) for num in nums]
        res = 0

        for index in range(num_len):
            counter = Counter()
            for num in nums:
                counter[num[index]] += 1

            size = len(counter)
            counts = list(counter.values())
            for i in range(size):
                for j in range(i + 1, size):
                    res += counts[i] * counts[j]

        return res
