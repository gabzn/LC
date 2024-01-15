https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:    
        player_lose_record = {}
        for winner, loser in matches:
            if winner not in player_lose_record:
                player_lose_record[winner] = [0]
            if loser not in player_lose_record:
                player_lose_record[loser] = [0]
        
            player_lose_record[loser][0] += 1
        
        res = [[], []]
        for player, record in sorted(player_lose_record.items()):
            # No losses
            if record[0] == 0:
                res[0].append(player)
                
            # One loss
            if record[0] == 1:
                res[1].append(player)
        
        return res
