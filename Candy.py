https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        LEN = len(ratings)
        candies = [1 for _ in range(LEN)]
        
        for i in range(1, LEN):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in range(LEN-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)
