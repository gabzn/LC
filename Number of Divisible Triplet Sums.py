https://leetcode.com/problems/number-of-divisible-triplet-sums/

class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        LEN = len(nums)
        
        remainder_map = defaultdict(list)
        for idx, num in enumerate(nums):
            remainder = num % d
            remainder_map[remainder].append(idx)
        
        res = 0
        """
        Fix i and j, and search for k
        If we want to make the sum of [i] and [j] + some number to be divisible by d, 
        we can just look at the remainder of ([i] + [j]) % d
        
        (3 + 4) % 5 = 1 
        To make (3 + 4 + [k]) divisible by 5, [k] % d == (d - 1) % d.
        In this case, [k] % d must be 4. 
        We find other numbers that have a remainder of 4 in the map.
        """
        for i in range(LEN):
            for j in range(i + 1, LEN):
                ij_sum = nums[i] + nums[j]
                
                remainder = ij_sum % d
                remainder_to_search = (d - remainder) % d
                
                if remainder_to_search in remainder_map:
                    indices = remainder_map[remainder_to_search]
                    first_index_greater_than_j = bisect_right(indices, j)
                    
                    res += (len(indices) - first_index_greater_than_j)
                
        return res
