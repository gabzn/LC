https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        fs, ft = Counter(s), Counter(t)
        return sum((fs - ft).values()) + sum((ft - fs).values())
