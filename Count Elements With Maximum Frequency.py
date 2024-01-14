https://leetcode.com/problems/count-elements-with-maximum-frequency/

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_freq = max(list(counter.values()))
        res = 0
        
        for _, f in counter.items():
            if f == max_freq:
                res += f
                
        return res
