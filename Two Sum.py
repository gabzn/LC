class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()

        for index, num in enumerate(nums):
            difference = target - num
            if difference in num_dict:
                return index, num_dict[difference]
        
            num_dict[num] = index
            
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        
        # We are putting the current num and its index into the dict.
        complement_dict = dict()

        # We assume the number we are looking at is 1 of the 2 numbers.
        # So, to find the other number AKA the complement, we want to know if the complement is one of the keys in the dict.
        for index, num in enumerate(nums):
            complement = target - num
                
            if complement in complement_dict.keys():
                return [index, complement_dict[complement]]
            
            complement_dict[num] = index
