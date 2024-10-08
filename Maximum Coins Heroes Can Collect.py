https://leetcode.com/problems/maximum-coins-heroes-can-collect/

class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        mcs = sorted([[m, c] for m, c in zip(monsters, coins)])
        for i in range(1, len(monsters)):
            _, prev_c = mcs[i - 1]
            mcs[i][1] += prev_c
                
        res = []
        for h in heroes:
            i = bisect_right(mcs, h, key=lambda x: x[0])
            if i == 0:
                res.append(0)
            else:
                res.append(mcs[i - 1][1])
        return res
