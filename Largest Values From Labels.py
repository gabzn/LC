https://leetcode.com/problems/largest-values-from-labels/
  
from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        value_label_dict = defaultdict(list)
        label_uselimit_dict = defaultdict(list)
        score = 0
        
        # Use a dict to keep track of the labels of each value
        for val, label in zip(values, labels):
            value_label_dict[val].append(label)
        
        # Sort the array so we can greedily pick the large values
        values.sort(reverse=True)        
        
        # Before picking a value, check to see if its label has been used up
        for val in values:
            label = value_label_dict[val].pop()
            
            if len(label_uselimit_dict[label]) < useLimit:
                label_uselimit_dict[label].append(val)
                score += val
                numWanted -= 1
                if not numWanted:
                    break
            
        return score
