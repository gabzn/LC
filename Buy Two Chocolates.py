https://leetcode.com/problems/buy-two-chocolates/

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first_smallest = second_smallest = 101
        
        for price in prices:
            if price <= first_smallest:
                second_smallest = first_smallest
                first_smallest = price
            else:
                second_smallest = min(second_smallest, price)
        
        return money if first_smallest + second_smallest > money else money - first_smallest - second_smallest
