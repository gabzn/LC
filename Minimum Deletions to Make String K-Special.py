https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        frequencies = Counter(word).values()
        max_keeps = 0
        
        for i, lower_bound_to_keep in enumerate(frequencies):
            keeps = 0
            upper_bound_to_keep = lower_bound_to_keep + k
            
            for freq in frequencies:
                if freq >= lower_bound_to_keep:
                    keeps += min(upper_bound_to_keep, freq)
            
            max_keeps = max(max_keeps, keeps)
        
        # Minimum deletions = Total length - Maximum keeps
        return len(word) - max_keeps
-------------------------------------------------------------------------------
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        frequencies = Counter(word).values()
        min_deletions = inf
        
        for idx, min_feq_to_keep in enumerate(frequencies):
            deletions = 0
            max_freq_to_keep = min_feq_to_keep + k
            
            for freq in frequencies:
                # If the current char has fewer than the min we need, delete it all
                if freq < min_feq_to_keep:
                    deletions += freq
                    continue
                
                # If the current char has way more than the max we need, delete the difference
                if freq > max_freq_to_keep:
                    deletions += freq - max_freq_to_keep
            
            min_deletions = min(min_deletions, deletions)
                
        return min_deletions
