https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        counter1, counter2 = Counter(word1), Counter(word2)
        
        # This takes care of operation 1
        # If the frequencies are the same, 
        # we can always attain one from the other by swapping chars multiple times.
        if counter1 == counter2:
            return True
        
        # If the code gets here, that means O1 fails
        # Try O2 by looking at the frequencies
        counter1 = dict(sorted(counter1.items(), key=lambda item: item[1]))
        counter2 = dict(sorted(counter2.items(), key=lambda item: item[1]))
        
        # Return false if any of the two conditions is met
        #   counts are not the same
        #   chars are not the same and one of them doesn't exist in the other
        for (char1, count1), (char2, count2) in zip(counter1.items(), counter2.items()):
            if (count1 != count2) or (char1 != char2 and char2 not in counter1):
                return False
                
        return True
