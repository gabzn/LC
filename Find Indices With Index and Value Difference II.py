https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/
https://www.youtube.com/watch?v=IKyFGYLa1is

class Solution:
    def findIndices(self, nums: List[int], idx_diff: int, val_diff: int) -> List[int]:
        LEN = len(nums)
        if LEN == 1:
            if idx_diff == 0 and val_diff == 0:
                return [0, 0]
            return [-1, -1]
        
        # Compute the prefix min [num, idx]
        prefix_min = [(nums[0], 0) if nums[0] <= nums[1] else (nums[1], 1)]
        for idx in range(1, LEN):
            if nums[idx] < prefix_min[-1][0]:
                prefix_min.append((nums[idx], idx))
            else:
                prefix_min.append(prefix_min[-1])
        
        # Compute the prefix max [num, idx]
        prefix_max = [(nums[0], 0) if nums[0] >= nums[1] else (nums[1], 1)]
        for idx in range(1, LEN):
            if nums[idx] > prefix_max[-1][0]:
                prefix_max.append((nums[idx], idx))
            else:
                prefix_max.append(prefix_max[-1])
        
        # Go through nums and find if there exists a pair idx_diff away that satifies the condition
        for j in range(idx_diff, LEN):
            i = j - idx_diff
            
            if abs(nums[j] - prefix_min[i][0]) >= val_diff and j - prefix_min[i][1] >= idx_diff:
                return [prefix_min[i][1], j]
            
            if abs(prefix_max[i][0] - nums[j]) >= val_diff and j - prefix_max[i][1] >= idx_diff:
                return [prefix_max[i][1], j]
            
        return [-1, -1]
