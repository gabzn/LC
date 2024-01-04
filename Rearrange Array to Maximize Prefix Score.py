https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        pref = [nums[0]]
        res = 0 if pref[0] <= 0 else 1
        
        for num in nums[1:]:
            pref.append(pref[-1] + num)
            if pref[-1] > 0:
                res += 1
        
        return res
