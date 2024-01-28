https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Brute force to find the next number
        def dfs(base, power, l):
            x = pow(base, power)
            if x in counter:
                if counter[x] == 1:
                    return l + 1
                else:
                    return dfs(base, power * 2, l + 2)
            else:
                return l - 1
                    
        counter = Counter(nums)            
        res = 1
        
        for num, count in counter.items():
            if num != 1 and count >= 2:
                res = max(res, dfs(num, 2, 2))
        
        # Edge case when there are 1's in nums
        if 1 in counter:
            res = max(res, counter[1] - 1 if counter[1] % 2 == 0 else counter[1])
        
        return res
