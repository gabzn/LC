https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, left: List[int], right: List[int]) -> int:
        def get_prefix_set(nums):
            pref = set()
            for num in nums:
                num_str = str(num)
                for i in range(len(num_str)):
                    pref.add(num_str[: i+1])
            return pref
        
        left_pref, right_pref = map(get_prefix_set, [left, right])    
        res = 0
    
        for num in left_pref.intersection(right_pref):
            res = max(res, len(num))
        
        return res
