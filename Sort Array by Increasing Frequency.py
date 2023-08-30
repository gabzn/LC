https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return sorted(nums, key=lambda num: (counter[num], -num))
