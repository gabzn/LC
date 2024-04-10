https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        
        deck.sort()
        queue = deque([i for i in range(N)])
        res = [-1] * N
        
        for card in deck:
            res[queue.popleft()] = card
            
            if queue:
                queue.append(queue.popleft())
        
        return res
