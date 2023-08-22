https://leetcode.com/problems/find-the-longest-equal-subarray/

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
                    right += 1
                # Backtrack one step because after the while loop right is out of bound
                right -= 1
                
                res = max(res, right - left + 1)
                left += 1
                    
        return res 
