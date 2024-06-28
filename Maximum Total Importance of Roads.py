https://leetcode.com/problems/maximum-total-importance-of-roads/

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1

        value = n
        res = 0
        for d in sorted(degree, reverse=True):
            res += value * d
            value -= 1

        return res
