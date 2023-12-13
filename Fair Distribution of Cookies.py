https://leetcode.com/problems/fair-distribution-of-cookies/
https://www.youtube.com/watch?v=t-BOmhv0WTw

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
