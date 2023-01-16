https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.backtrack(nums, [], [], set())
    
    def backtrack(self, nums, current, res, visited_indices):
        if len(current) == len(nums):
            res.append(current.copy())
            return res
        
        for ind in range(len(nums)):
            if ind in visited_indices:
                continue
            if ind > 0 and nums[ind] == nums[ind - 1] and (ind - 1) not in visited_indices:
                continue
            
            current.append(nums[ind])
            visited_indices.add(ind)
            res = self.backtrack(nums, current, res, visited_indices)
            
            # Clean up
            current.pop()
            visited_indices.remove(ind)
        
        return res
-----------------------------------------------------------------------------------------------------------
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        return self.backtrack(counter, [], [], len(nums))
    
    def backtrack(self, counter, current, res, N):
        if len(current) == N:
            res.append(current.copy())
            return res
        
        for num in counter:
            if counter[num] > 0:
                current.append(num)
                counter[num] -= 1
                res = self.backtrack(counter, current, res, N)
                
                current.pop()
                counter[num] += 1
        
        return res
