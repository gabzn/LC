https://leetcode.com/problems/maximize-greatness-of-an-array/

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        LEN = len(nums)
        
        ascending = sorted(nums)
        descending = ascending[::-1]
        
        res = 0
        descending_ptr = 0
        ascending_ptr = LEN - 1
        
        while descending_ptr < LEN and ascending_ptr > -1:
            if descending[descending_ptr] > ascending[ascending_ptr]:
                res += 1
                descending_ptr += 1
                ascending_ptr -= 1
            else:
                ascending_ptr -= 1
            
        return res
