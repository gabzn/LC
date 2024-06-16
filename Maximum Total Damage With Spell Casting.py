https://leetcode.com/problems/maximum-total-damage-with-spell-casting/


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = sorted(Counter(power).items())
        n = len(counter)

        # dp[i] = max damage from 0 to i
        dp = [0] * n
        j = 0
        
        for i in range(n):
            spell, count = counter[i]
            while counter[j][0] <= spell - 3:
                j += 1
            
            take = (spell * count) + (0 if j - 1 < 0 else dp[j-1])
            skip = 0 if i == 0 else dp[i-1]

            dp[i] = max(take, skip)
        
        return dp[-1]
----------------------------------------------------------------------
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = sorted(Counter(power).items())
        n = len(counter)

        # dp[i] = max damage from 0 to i
        dp = [0] * n

        for i in range(n):
            spell, count = counter[i]
            j = i
            while j >= 0 and counter[j][0] + 2 >= spell:
                j -= 1

            take = (spell * count) + (0 if j < 0 else dp[j])
            skip = 0 if i == 0 else dp[i-1]

            dp[i] = max(take, skip)

        return dp[-1]
----------------------------------------------------------------------
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
