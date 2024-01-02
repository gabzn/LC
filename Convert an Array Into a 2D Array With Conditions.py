https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        LEN = len(nums)
        
        nums.sort()
        res = []
        i = 0
        
        while i < LEN:
            j = i
            insertion_index = 0
            
            while j < LEN and nums[i] == nums[j]:
                if insertion_index == len(res):
                    res.append([nums[j]])
                else:
                    res[insertion_index].append(nums[j])
                
                j += 1
                insertion_index += 1
            
            i = j
        
        return res
