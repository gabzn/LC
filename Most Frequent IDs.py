https://leetcode.com/problems/most-frequent-ids/

from sortedcontainers import SortedList

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        counter = Counter()
        sorted_counts = SortedList()
        res = []
        
        for id, f in zip(nums, freq):
            # Remove the previous count
            if counter[id]:
                sorted_counts.remove(counter[id])
            
            # Update the count
            counter[id] += f
            
            # Add it back to the count if the new count is not 0
            if counter[id]:
                sorted_counts.add(counter[id])
                
            res.append(sorted_counts[-1] if sorted_counts else 0)
            
        return res
