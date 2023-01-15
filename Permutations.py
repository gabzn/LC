https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(nums, [], [], set())
    
    def backtrack(self, nums, current, res, visited_nums):
        if len(current) == len(nums):
            res.append(current.copy())
            return res
        
        for num in nums:
            if num not in visited_nums:
                visited_nums.add(num)
                current.append(num)
                res = self.backtrack(nums, current, res, visited_nums)
                
                # Clean up
                current.pop()
                visited_nums.remove(num)
            
        return res
-------------------------------------------------------------------------------------------------
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
