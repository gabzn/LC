https://leetcode.com/problems/smallest-string-with-swaps/
  
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return
            
            if rank[root_x] == rank[root_y]:
                root[root_y] = root_x
                rank[root_x] += 1
            elif rank[root_x] > rank[root_y]:
                root[root_y] = root_x
            else:
                root[root_x] = root_y
                
        if len(pairs) == 0:
            return s
        
        N = len(s)
        root = [i for i in range(N)]
        rank = [1 for _ in range(N)]
        
        # Group all the indices into a group
        for a, b in pairs:
            union(a, b)
          
        # Adjust the root to absolute root
        for idx in range(N):
            root[idx] = find(root[idx])
                    
        # Loop through s. For each index we want to know what group it's in by looking up the root list
        # then we store the groups in a dict.
        groups = collections.defaultdict(list)
        for idx, char in enumerate(s):
            r = root[idx]
            heapq.heappush(groups[r], char)
                
        # Loop from 0 to N to build the answer.
        res = ''
        for i in range(N):
            r = root[i]
            res += heapq.heappop(groups[r])
        
        return res
