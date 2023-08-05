https://leetcode.com/problems/largest-number/

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for index in range(len(nums)):
            nums[index] = str(nums[index])
            
        res = ''.join(sorted(nums, key=LargerNumKey))
        
        return res if res[0] != '0' else '0'
