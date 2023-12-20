https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def is_palindromic(x):
            return x == x[::-1]
        
        LEN = len(nums)
        
        nums.sort()
        
        mid = nums[LEN // 2]
        low = int(math.floor(mid))
        high = int(math.ceil(mid))
        
        while not is_palindromic(str(low)):
            low -= 1
        
        while not is_palindromic(str(high)):
            high += 1
        
        low_cost = high_cost = 0
        for num in nums:
            low_cost += abs(low - num)
            high_cost += abs(high - num)

        return min(low_cost, high_cost)
--------------------------------------------------------------------------------------------
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        """
        1: choose a num in nums and X
        2: add |num - X| to total cost
        3: set num to X
        
        How to find  X ????
        """
        def is_palindromic(x):
            return x == x[::-1]
        
        LEN = len(nums)
        
        nums.sort()
        
        mid = nums[LEN // 2] if LEN % 2 == 1 else (nums[LEN // 2 - 1] + nums[LEN // 2]) / 2
        low = int(math.floor(mid))
        high = int(math.ceil(mid))
        
        while not is_palindromic(str(low)):
            low -= 1
        
        while not is_palindromic(str(high)):
            high += 1
        
        low_cost = high_cost = 0
        for num in nums:
            low_cost += abs(low - num)
            high_cost += abs(high - num)

        return min(low_cost, high_cost)
