https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sums = [0]
        for index in range(1, len(nums)):
            left_sums.append(left_sums[-1] + nums[index - 1])
        
        nums.reverse()
        
        right_sums = [0]
        for index in range(1, len(nums)):
            right_sums.append(right_sums[-1] + nums[index - 1])
        right_sums.reverse()
        
        
        return [abs(a - b) for a, b in zip(left_sums, right_sums)]
