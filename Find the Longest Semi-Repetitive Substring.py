https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        # Handle the case when len(s) == 1
        res = 1
        left = 0
        pair_count = 0

        for right in range(1, len(s)):
            pair_count += (s[right] == s[right - 1])

            # There are 2 pairs of same digit, move the left until we have 1 pair left.
            while pair_count == 2:
                # Found the previous pair.
                if s[left] == s[left + 1]:
                    pair_count = 1
                left += 1

            res = max(res, right - left + 1)

        return res
