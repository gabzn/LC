https://leetcode.com/problems/alice-and-bob-playing-flower-game/

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        odd_x = ceil(n / 2)
        even_x = n // 2
        
        odd_y = ceil(m / 2)
        even_y = m // 2
        
        return (odd_x * even_y) + (even_x * odd_y)

class Solution:
    def flowerGame(self, n: int, m: int) -> int:        
        return (n * m) // 2
