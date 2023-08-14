https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:  
        LEN = len(nums)
        res = 0
        prefix = [0]
        
        for num in nums:
            prefix.append(prefix[-1] + num)

        """
        nums[: l] will be left    ->        pref[l]
        nums[l + 1: r + 1] will be mid ->   pref[r] - pref[l]
        nums[r + 1:] will be right     ->   pref[-1] - pref[r]        
        
        At every index i in prefi, find all j such that:
            prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j]
              left              mid                     right
            
        prefix[i] <= prefix[j] - prefix[i] becomes 2 * prefix[i] <= prefix[j]
        prefix[j] - prefix[i] <= prefix[-1] - prefix[j] becomes prefix[j] <= (prefix[-1] + prefix[i]) // 2
        """
        for i in range(1, LEN):
            left_bound_j = bisect_left(prefix, 2 * prefix[i])
            right_bound_j = bisect_right(prefix, (prefix[-1] + prefix[i]) // 2)
            
            # Normally, we just need to do right_bound_j - left_bound_j to find the number of ways
            # When i reaches the second to last index in prefix, 
            # left_bound_j and right_bound_j will be out of bound meaning LEN + 1
            res += max(0, min(right_bound_j, LEN) - max(left_bound_j, i+1))
            
        return res % (10**9 + 7)    
