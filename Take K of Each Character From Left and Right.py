https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Instead of finding the min window needed to get >= k for each char,
        # we keep adding chars to a window as long as it's still allowed.
        # For each char, the max we can put in a max window is total - k
        # because we want the min window to have exactly k of each char only.
        total_counter = Counter(s)
        if total_counter['a'] < k or total_counter['b'] < k or total_counter['c'] < k:
            return -1

        max_char_to_be_allowed_in_window = {
            'a': max(total_counter['a'] - k, 0),
            'b': max(total_counter['b'] - k, 0),
            'c': max(total_counter['c'] - k, 0),
        }
        window_counter = Counter()
        res = 0
        left = 0

        for right, char in enumerate(s):
            window_counter[char] += 1

            while window_counter[char] > max_char_to_be_allowed_in_window[char]:
                to_remove = s[left]
                window_counter[to_remove] -= 1
                if window_counter[to_remove] == 0:
                    del window_counter[to_remove]
                left += 1

            res = max(right - left + 1, res)

        return len(s) - res
