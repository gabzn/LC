https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        N, M = map(len, [s, goal])
        if N != M:
            return False

        for i in range(N):
            new_s = s[i + 1:] + s[: i + 1]
            if new_s == goal:
                return True

        return False
