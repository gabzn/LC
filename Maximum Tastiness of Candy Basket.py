https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def can_get_at_least_k_candies_with_min_diff_of_mid(diff):
            candy = 0
            last = -inf
            
            for x in price:
                if x - last >= diff:
                    candy += 1
                    last = x
            
            return candy >= k

        N = len(price)

        price.sort()
        left = -1
        right = 10 ** 15

        while left + 1 != right:
            mid = (left + right) // 2

            if can_get_at_least_k_candies_with_min_diff_of_mid(mid):
                left = mid
            else:
                right = mid

        return left
--------------------------------------------------------------------------------
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def can_get_at_least_k_candies_with_min_diff_of_mid(diff):
            count = 1
            i = 0
            
            while i < N:
                j = i + 1

                while (j < N) and (price[j] - price[i] < diff):
                    j += 1
                
                if j == N:
                    break
                
                count += 1
                i = j

            return count >= k

        N = len(price)

        price.sort()
        left = -1
        right = 10 ** 15

        while left + 1 != right:
            mid = (left + right) // 2

            if can_get_at_least_k_candies_with_min_diff_of_mid(mid):
                left = mid
            else:
                right = mid

        return left
