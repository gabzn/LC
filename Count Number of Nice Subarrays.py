https://leetcode.com/problems/count-number-of-nice-subarrays/
https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        res = 0
        pref_count = defaultdict(int)
        pref_count[0] = 1

        for i in range(N):
            nums[i] = (nums[i] % 2 == 1)
            if i > 0:
                nums[i] += nums[i-1]
            
            num = nums[i]
            diff = num - k
            if diff in pref_count:
                res += pref_count[diff]
            
            pref_count[num] += 1
            
        return res
