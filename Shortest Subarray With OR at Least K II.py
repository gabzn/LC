https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = inf
        or_val = 0
        left = 0
        bit_counts = [0] * 31
        
        for right in range(N):
            
            # Get the bits of nums[right]
            for bit in range(31):
                if (nums[right] & (1 << bit)):
                    bit_counts[bit] += 1
                    or_val |= (1 << bit)
            
            # If or_val is too large, shrink the window
            while left <= right and or_val >= k:
                res = min(res, right - left + 1)
                
                for bit in range(31):
                    if (nums[left] & (1 << bit)):
                        bit_counts[bit] -= 1
                        
                        # Only turn off the bit if there are no more
                        if bit_counts[bit] == 0:
                            or_val ^= (1 << bit)
                
                left += 1
        
        return res if res != inf else -1
