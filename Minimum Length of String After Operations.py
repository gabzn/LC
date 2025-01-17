https://leetcode.com/problems/minimum-length-of-string-after-operations

class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        total = len(s)
        chars_removed = 0
        for _, count in counter.items():
            if count >= 3:
                div = (count - 1) // 2
                chars_removed += 2 * div
        return total - chars_removed
