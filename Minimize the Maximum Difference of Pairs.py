https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        def can_find_p_pairs_leq_to(m):
            pairs, index = 0, 0
            
            while index < LEN - 1:
                
            # Maximum Difference means less than or equal to (<=) m
            # If m is 2, and a difference of a pair is 0, this pair will count
                if nums[index + 1] - nums[index] <= m:
                    pairs += 1
                    index += 1
                index += 1
        
            return pairs >= p
        
        LEN = len(nums)
        nums.sort()
        
        l, r = -1, nums[-1] - nums[0] + 1
        
        while l + 1 != r:
            m = (l + r) // 2
            
            # Now we want to minimize m. 
            # If you can find p pairs <= m, you can always find p pairs <= (any num greater or equal to m)
            if can_find_p_pairs_leq_to(m):
                r = m
            else:
                l = m
        
        return r
