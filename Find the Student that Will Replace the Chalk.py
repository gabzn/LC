https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k = k % total_chalk
        
        for i, c in enumerate(chalk):
            if k < c:
                return i
            k -= c
