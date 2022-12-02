https://leetcode.com/problems/permutations/
  
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.solve(nums, res, [], set())
        return res

    def solve(self, nums, res, permutation, used_nums):
        if len(permutation) == len(nums):  # Goal is when all nums have been used
            res.append(permutation[:])     # list[:] = list.copy()
            return
        
        # Explore every choice using a for loop
        for num in nums:            
            if num not in used_nums:       # Check if this choice is valid
                permutation.append(num)    # If valid, use it
                used_nums.add(num)         # Mark it as used
                self.solve(nums, res, permutation, used_nums)    # Recursive call
                
                # After it's been used, remove/restore it.
                used_nums.remove(num)      
                permutation.pop()         
