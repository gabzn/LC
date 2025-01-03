https://leetcode.com/classic/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        VOWELS = set(list('aeiou'))
        N = len(words)
        pref = [0] * (N + 1)
        for i, word in enumerate(words):
            cnt = 1 if word[0] in VOWELS and word[-1] in VOWELS else 0
            pref[i + 1] = pref[i] + cnt
        return [pref[end + 1] - pref[start] for start, end in queries]
