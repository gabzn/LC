https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

class Solution:
    def minAnagramLength(self, s: str) -> int:
        N = len(s)

        total_count = Counter(s)
        current_count = Counter()

        for l, char in enumerate(s, 1):
            if l > N // 2:
                return N
            
            current_count[char] += 1
            if len(total_count) != len(current_count):
                continue

            times = 0
            good = True
            for char in total_count:
                # Every (total_count[char] // current_count[char]) has to be the same
                # Every (total_count[char] // current_count[char]) has to be divisble
                div, mod = divmod(total_count[char], current_count[char])
                if times == 0:
                    times = div

                if times != div or mod != 0:
                    good = False
                    break

            if good:
                return l
