https://leetcode.com/problems/permutation-in-string/
https://leetcode.com/problems/find-all-anagrams-in-a-string/
  
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter_1 = Counter(s1)
        counter_2 = Counter()
        for i, char in enumerate(s2):
            counter_2[char] += 1

            left = i + 1 - len(s1)
            if left < 0:
                continue

            if counter_1 == counter_2:
                return True

            counter_2[s2[left]] -= 1
            if counter_2[s2[left]] == 0:
                del counter_2[s2[left]]

        return False
