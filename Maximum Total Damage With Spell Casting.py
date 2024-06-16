https://leetcode.com/problems/maximum-total-damage-with-spell-casting/


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        @cache
        def dp(i):
            if i < 0:
                return 0

            skip = dp(i - 1)

            spell, freq = lst[i]
            j = i
            while j >= 0 and lst[j][0] + 2 >= spell:
                j -= 1
            take = (spell * freq) + dp(j)

            return max(skip, take)

        lst = sorted(Counter(power).items())
        return dp(len(lst) - 1)
---------------------------------------------------------------
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        @cache
        def dp(i):
            if i < 0:
                return 0

            skip = dp(i - 1)

            spell, freq = lst[i]
            j = bisect_left(lst, spell - 2, key=lambda x: x[0])
            take = (spell * freq) + dp(j - 1)

            return max(skip, take)

        lst = sorted(Counter(power).items())
        return dp(len(lst) - 1)
