https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies

class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        counter = Counter(candies)
        if k == 0:
            return len(counter)

        res = 0

        for right, flavor in enumerate(candies):
            counter[flavor] -= 1
            if counter[flavor] == 0:
                del counter[flavor]

            left = right + 1 - k
            if left < 0:
                continue
            res = max(res, len(counter))
            counter[candies[left]] += 1

        return res
