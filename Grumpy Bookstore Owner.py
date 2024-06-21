https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers)
        
        # Find the # number of satisfied customers when the owner is not grumpy && not using any trick
        satisfied_customers_without_using_trick = 0
        for customer, is_grumpy in zip(customers, grumpy):
            if is_grumpy == 0:
                satisfied_customers_without_using_trick += customer
        
        # Find the max # of satisfied customers when the owner is using trick
        # We only consider the customers that are not satisfied AKA when the owner is grumpy
        max_satisfied_customers_with_trick = 0
        satisfied_customers_with_trick = 0
        left = right = 0
        while right < N:
            if right - left >= minutes:
                if grumpy[left] == 1:
                    satisfied_customers_with_trick -= customers[left]
                
                left += 1
            
            if grumpy[right] == 1:
                satisfied_customers_with_trick += customers[right]
            
            max_satisfied_customers_with_trick = max(max_satisfied_customers_with_trick, satisfied_customers_with_trick)
            right += 1
        
        return satisfied_customers_without_using_trick + max_satisfied_customers_with_trick
