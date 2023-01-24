https://leetcode.com/problems/find-the-town-judge/
  
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_degree = [0] * n
        in_degree = [0] * n
        
        for a, b in trust:
            out_degree[a-1] += 1
            in_degree[b-1] += 1

        # The judge has 0 out_degree because he trusts no one
        # and has n - 1 in_degree becasue everyone else trusts him
        for i in range(n):
            if out_degree[i] == 0 and in_degree[i] == n - 1:
                return i + 1
        
        return -1
