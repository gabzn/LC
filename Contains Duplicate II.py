https://leetcode.com/problems/contains-duplicate-ii/
  
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_idx_dict = collections.defaultdict(int)
        
        for i in range(len(nums)):
            num = nums[i]
            if num in num_idx_dict and abs(i - num_idx_dict[num]) <= k:
                return True
            
            num_idx_dict[num] = i
            
        return False
