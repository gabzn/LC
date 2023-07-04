https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        for num, freq in counter.items():
            if freq == 1:
                return num
