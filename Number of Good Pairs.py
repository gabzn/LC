https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        
        for _, count in counter.items():
            res += (count * (count-1)) // 2
        
        return res
