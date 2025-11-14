https://leetcode.com/problems/find-the-longest-equal-subarray/

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        res = 1
        cur_longest = 1
        left = 0

        for right, num in enumerate(nums):
            counter[num] += 1

            # Only move the left when num's frequency is higher 
            # and we don't have enough k to delete other nums that are not num.
            while counter[num] > cur_longest and (right - left + 1) - counter[num] > k:
                counter[nums[left]] -= 1
                left += 1

            # After making the window smaller, we check if num is still the longest.
            res = max(res, counter[num])
            cur_longest = max(cur_longest, res)

        return res
___________________________________________________________________
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        res = 0
        
        num_indices = defaultdict(list)
        for index, num in enumerate(nums):
            num_indices[num].append(index)
        
        for num, indices in num_indices.items():
            LEN = len(indices)
            
            left, right = 0, 0
            while left < LEN:
                # (indices[right] - indices[left] + 1) is the how many numbers between right and left
                # (right - left + 1) is the count of num
                while right < LEN and (indices[right] - indices[left] + 1) - (right - left + 1) <= k:
                    res = max(res, right - left + 1)
                    right += 1
                
                left += 1
                    
        return res
