https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/description/

class Solution:
    def maxFreq(self, s: str, max_letters: int, min_size: int, max_size: int) -> int:
        substring_counter = Counter()
        unique_char_counter = Counter()

        for i in range(len(s)):
            char = s[i]
            unique_char_counter[char] += 1

            # We only need to look at substring of length min_size:
            # 1. longer the substring, more unique chars
            # 2. every substring of min_size is contained within a longer substring
            left = i + 1 - min_size

            # Not long enough to form a window yet
            if left < 0:
                continue
            
            # We have a valid substring
            unique_chars = len(unique_char_counter)
            if unique_chars <= max_letters:
                substring_counter[s[left: i + 1]] += 1

            char = s[left]
            unique_char_counter[char] -= 1
            if unique_char_counter[char] == 0:
                del unique_char_counter[char]

        return max(substring_counter.values(), default=0)
