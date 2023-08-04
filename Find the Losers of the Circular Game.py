https://leetcode.com/problems/find-the-losers-of-the-circular-game/

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        players = set()
        cur_player, turn = 0, 1
        
        while cur_player not in players:
            players.add(cur_player)
            cur_player = (cur_player + (turn * k)) % n
            turn += 1
            
        res = []
        for i in range(n):
            if i not in players:
                res.append(i + 1)
        
        return res
