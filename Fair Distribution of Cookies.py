https://leetcode.com/problems/fair-distribution-of-cookies/
https://www.youtube.com/watch?v=t-BOmhv0WTw

class Solution:
    def distributeCookies(self, cookies: List[int], children: int) -> int:
        def can_distribute_at_most_mid_cookies_to_children(assignments, index, mid):
            if index == LEN:
                return True
            
            for child in range(children):
                if assignments[child] + cookies[index] > mid:
                    continue
                
                assignments[child] += cookies[index]
                
                if can_distribute_at_most_mid_cookies_to_children(assignments, index + 1, mid):
                    return True
                
                assignments[child] -= cookies[index]
            
            return False
        
        LEN = len(cookies)
        left, right = max(cookies) - 1, sum(cookies) + 1
        
        while left + 1 != right:
            mid = (left + right) // 2
            assignments = [0 for _ in range(children)]
            
            if can_distribute_at_most_mid_cookies_to_children(assignments, 0, mid):
                right = mid
            else:
                left = mid
        
        return right
-------------------------------------------------------------------------------
class Solution:
    def distributeCookies(self, cookies: List[int], children: int) -> int:
        LEN = len(cookies)
        INF = math.inf
        assignments = [0 for _ in range(children)]
        
        def backtrack(index, num_children_do_not_have_cookies):
            # Reach the end, return the unfairness
            if index == LEN:
                return max(assignments)
            if num_children_do_not_have_cookies > LEN - index:
                return INF
            
            max_cookies = INF
            
            # Go through each child and give them cookies
            for child in range(children):
                if assignments[child] == 0:
                    num_children_do_not_have_cookies -= 1
                assignments[child] += cookies[index]
                
                max_cookies = min(max_cookies, backtrack(index + 1, num_children_do_not_have_cookies))
                                
                assignments[child] -= cookies[index]
                if assignments[child] == 0:
                    num_children_do_not_have_cookies += 1
            
            return max_cookies
                
        return backtrack(0, children)
