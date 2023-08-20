https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        used_nums, res = 0, 0
        no_good_set = set()
        
        for num in range(1, 100):
            if num not in no_good_set:
                res += num
                
                # Early terminate
                used_nums += 1
                if used_nums == n:
                    return res
                    
                # Add the diff into the set because we don't want the diff
                no_good_set.add(k - num)
