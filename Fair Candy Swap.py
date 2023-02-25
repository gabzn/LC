https://leetcode.com/problems/fair-candy-swap/
  
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_candies, bob_candies = sum(aliceSizes), sum(bobSizes)
        bob_set = set(bobSizes)
        
        for x in aliceSizes:
            y = (bob_candies - alice_candies + (2 * x)) // 2
            if y in bob_set:
                return [x, y] 
