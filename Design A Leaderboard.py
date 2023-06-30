https://leetcode.com/problems/design-a-leaderboard/

class Leaderboard:

    def __init__(self):
        self.board = defaultdict(int)
        
    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        k_score = 0
        
        # Use a heap to keep track of the top K scores
        for score in self.board.values():
            heappush(heap, score)
            k_score += score
            
            # If the size is larger than K, pop the smallest score to keep the size K
            if len(heap) > K:
                k_score -= heappop(heap)
                
        return k_score
        
    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0
-------------------------------------------------------------------------------------
class Leaderboard:

    def __init__(self):
        self.board = defaultdict(int)
        
    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score

    def top(self, K: int) -> int:
        scores = list(self.board.values())
        scores.sort(reverse=True)
        k_score, index = 0, 0
        
        while index < K:
            k_score += scores[index]
            index += 1
        
        return k_score
        
    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0
