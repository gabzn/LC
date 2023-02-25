https://leetcode.com/problems/longest-subsequence-with-limited-sum/
  
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        
        ans = []
        for q in queries:
            l, r = 0, len(prefix_sum)
            
            while l < r:
                m = (l + r) // 2
                
                if prefix_sum[m] <= q:
                    l = m + 1
                else:
                    r = m
            
            ans.append(l)
            
        return ans
