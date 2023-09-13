https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:               
        # Keep track of the freq of each char within a window size
        freqs = defaultdict(int)
        running_sum, ans = 0, 0
        left, right = 0, 0
        
        while right < len(nums):
            freqs[nums[right]] += 1
            running_sum += nums[right]
            
            # If the window size is more than k, move left 1 unit to its right
            if right - left + 1 > k:
                freqs[nums[left]] -= 1
                running_sum -= nums[left]
                
                if freqs[nums[left]] == 0:
                    del freqs[nums[left]]    
                left += 1
            
            # If the window size is k and there's at least m distinct chars
            if right - left + 1 == k and len(freqs) >= m:
                ans = max(running_sum, ans)
            
            right += 1
                
        return ans
------------------------------------------------------------------------------
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:        
        LEN = len(nums)
        
        # Compute prefix sum
        pref = [0]
        for num in nums:
            pref.append(pref[-1] + num)

        # Check all subarrays of size k to see if each has at least m unique numbers
        ans = 0
        for right in range(k-1, LEN):
            left = right - k + 1
            
            unique_nums = len(set(nums[left: right+1]))
            if unique_nums >= m:
                subarray_sum = pref[right+1] - pref[left]
                ans = max(subarray_sum, ans)
                
        return ans
