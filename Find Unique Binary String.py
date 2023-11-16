https://leetcode.com/problems/find-unique-binary-string/


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        LEN = len(nums)
        nums = set(nums)
        
        def backtrack(i, cur):
            if i == LEN: 
                return None if cur in nums else cur
            
            res = backtrack(i + 1, cur + "0")
            if res: 
                return res
            
            res = backtrack(i + 1, cur + "1")
            if res: 
                return res 
        
        return backtrack(0, "")
---------------------------------------------------------------------
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        
        for i in range(len(nums)):
            if nums[i][i] == '1':
                res.append('0')
            else:
                res.append('1')
        
        return "".join(res)
