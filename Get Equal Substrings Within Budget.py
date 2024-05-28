https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, max_cost: int) -> int:
        N = len(s)
        
        costs = [0] * N
        res = current_cost = left = 0
        
        for right in range(N):            
            cost = abs(ord(s[right]) - ord(t[right]))
            costs[right] = cost
            current_cost += cost
            
            while current_cost > max_cost:
                current_cost -= costs[left]
                left += 1
                
            res = max(res, right - left + 1)
        
        return res
