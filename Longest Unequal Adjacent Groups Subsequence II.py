https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

class Solution:
    def getWordsInLongestSubsequence(self, LEN: int, words: List[str], groups: List[int]) -> List[str]: 
        @cache
        def dfs(idx):
            if idx == LEN:
                return 0
            
            max_len = 1
            next_i = -1
            
            for i in reachable_nodes_from_i[idx]:
                cur_len = 1 + dfs(i)
                
                if cur_len > max_len:
                    max_len = cur_len
                    next_i = i
            
            dp[idx] = max_len
            next_idx[idx] = next_i
            return max_len
        
        reachable_nodes_from_i = self.compute_reachable_nodes_from_each_idx(LEN, words, groups)
        dp = [0 for _ in range(LEN)]
        next_idx = [-1 for _ in range(LEN)]
        
        max_len, best_idx = 1, 0
        for idx in range(LEN):
            res = dfs(idx)
            
            if res > max_len:
                max_len = res
                best_idx = idx
        
        indices = [best_idx]
        while next_idx[best_idx] != -1:
            indices.append(next_idx[best_idx])
            best_idx = next_idx[best_idx]
        
        return [words[idx] for idx in indices]
     
    def compute_reachable_nodes_from_each_idx(self, LEN, words, groups):
        reachable_nodes_from_i = [[] for _ in range(LEN)]
        
        for i in range(LEN):
            for j in range(i + 1, LEN):
                if groups[i] == groups[j] or \
                   len(words[i]) != len(words[j]) or \
                   not self.is_hamming_distance_one(words[i], words[j]):
                    continue
                
                reachable_nodes_from_i[i].append(j)
        
        return reachable_nodes_from_i
    
    def is_hamming_distance_one(self, s1, s2):
        hamming_distance = 0
        
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                hamming_distance += 1
        
        return hamming_distance == 1    
