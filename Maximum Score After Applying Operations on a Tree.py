https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/
https://www.youtube.com/watch?v=mxJ0wqobW_c

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        @cache
        def dfs(node, skipped_already, parent):
            # Base case
            # If we skipped a node previously, we take the leaf node
            # Else we skip the leaf node
            if len(graph[node]) == 1 and graph[node][0] == parent:
                return values[node] if skipped_already else 0
            
            # Take the current node
            take = values[node]
            for child in graph[node]:
                if child == parent:
                    continue
                take += dfs(child, skipped_already, node)
            
            # Skip the current node
            skip = 0
            for child in graph[node]:
                if child == parent:
                    continue
                skip += dfs(child, True, node)
            
            return max(take, skip)
        
        return dfs(0, False, -1)
