https://leetcode.com/problems/reorganize-string/
  
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ''
        
        counter = collections.Counter(s)
        char_counts = [(-count, char) for char, count in counter.items()]
        heapify(char_counts)
        
        while char_counts:          
            # The reason we have placeholder is because we don't want to push the current char back to the heap immediately. 
            # Example: 10a 3b 2c, if we pop an 'a' and push it back to the heap. The heap becomes 9a 3b 2c.
            # Now, 'a' is still the most frequent char. 
            placeholder = []
            
            # Most of the time we want to pop 2 most frequent chars at a time so we can avoid 2 same letters next to each other.
            # If char_counts has only one count left, we pop once only.
            pop_times = min(2, len(char_counts))
            for _ in range(pop_times):
                count, letter = heappop(char_counts)
                
                # Every time we pop, we check if the last char in res is the same as the current char. If it is, return ''
                # Else, we append the current char to res.
                if res and res[-1] == letter:
                    return ''
                
                res += letter
                count += 1
                if count:
                    placeholder.append((count, letter))
                
            for count, letter in placeholder:
                heappush(char_counts, (count, letter))
            
        return res
