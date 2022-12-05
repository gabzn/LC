https://leetcode.com/problems/boats-to-save-people/
  
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
          Since we know for sure a person's weight is always going to be <= limit,
          we can be greedy and put all the heavier people in first.
          To do so, we need to sort the list.
        """
        people.sort()
        boats, l, r = 0, 0, len(people) - 1
        
        while l <= r:
            boats += 1
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            
        return boats
